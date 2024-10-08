import discord
from discord.ext import taks, commands
from discord import app_commands
from datatime import datetime,timedelta
import asynio
import json
import os

TOKEN = 'BOT TOKEN'

CONFIG_FILE = 'Soundwave.json'

BOT_OWNER_ID = MY_ID

intents = discord.Intetns.default()
intents.message_contents = True # Required for reading messsages
intents.guilds = True # Accessing Guild
intnets.members = True # Accessing members and roles

# Function to Load the JSON file
def load_settings():
  if not os.path.exists(CONFIG_FILE):
    return {"guilds": {}}

with open(CONFIG_FILE, 'r') as file:
  try:
    return json.load(file)
  except json.JSONDecodeError as e:
    print(f"Error loading settings: {e}")
            return {"guilds": {}}

# Save the JSON file
def save_setting(settings):
  with open(CONFIG_FILE, "w") as file:
    json.dump(settings, file, indent = 4)

# Load the File
settings = load_settings()

# Function to inttalise guild settings
def initialize_guild_settings(guild_id):
    if str(guild_id) not in settings['guilds']:
        settings['guilds'][str(guild_id)] = {
            "channel_id": None,
            "roles": {day: None for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
        }
        save_settings(settings)
        print(f"Initialized settings for guild {guild_id}.")

# Command to set the Soundwave Channel
@bot.tree.command(name="set_channel", description="Set the soundwave channel for this server.")
async def set_channel(interaction: discord.Interaction):
    initialize_guild_settings(interaction.guild.id)  # Ensure guild settings exist
    channel = interaction.channel  # Get the current channel
    settings['guilds'][str(interaction.guild.id)]['channel_id'] = channel.id
    save_settings(settings)
    await interaction.response.send_message(f"Soundwave channel set to {channel.mention}!")

# Command to set a role for a specific day (Only for users with "Soundwave Role")
@bot.tree.command(name="set_role", description="Assign a role to a specific day.")
@app_commands.describe(day="Day of the week", role="Role to assign")
async def set_role(interaction: discord.Interaction, day: str, role: discord.Role):
    # Check if the user has the "Soundwave Role"
    soundwave_role = discord.utils.get(interaction.guild.roles, name="Soundwave Role")

    if soundwave_role not in interaction.user.roles:
        await interaction.response.send_message("You don't have the required 'Soundwave Role' to use this command.", ephemeral=True)
        return

    valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if day not in valid_days:
        await interaction.response.send_message(f"Invalid day! Please choose from: {', '.join(valid_days)}")
        return

    initialize_guild_settings(interaction.guild.id)  # Ensure guild settings exist
    settings['guilds'][str(interaction.guild.id)]['roles'][day] = role.name
    save_settings(settings)
    await interaction.response.send_message(f"{role.name} has been assigned to {day}!")

# Command to display whose day it is today
@bot.tree.command(name="s-day", description="Displays whose day it is today!")
async def whose_day(interaction: discord.Interaction):
    now = datetime.utcnow()  # Get the current UTC time
    current_day = now.strftime("%A")  # Get the current day of the week

    initialize_guild_settings(interaction.guild.id)  # Ensure guild settings exist
    role_name = settings['guilds'][str(interaction.guild.id)]['roles'].get(current_day, None)

    if role_name:
        await interaction.response.send_message(f"Today is {role_name}'s day to post!")
    else:
        await interaction.response.send_message(f"No role is assigned for today.")

# Command to display whose day it is tomorrow
@bot.tree.command(name="s-tomorrow", description="Displays whose day it is tomorrow!")
async def whose_day_tomorrow(interaction: discord.Interaction):
    now = datetime.utcnow()  # Get the current UTC time
    tomorrow = now + timedelta(days=1)  # Calculate tomorrow's date
    tomorrow_day = tomorrow.strftime("%A")  # Get tomorrow's day of the week

    initialize_guild_settings(interaction.guild.id)  # Ensure guild settings exist
    role_name = settings['guilds'][str(interaction.guild.id)]['roles'].get(tomorrow_day, None)

    if role_name:
        await interaction.response.send_message(f"Tomorrow is {role_name}'s day to post!")
    else:
        await interaction.response.send_message(f"No role is assigned for tomorrow.")
      
# Commanf to display all days and rolles assigned to them 
@bot.tree.command(name="schedule", description="Displays the current role schedule for the week.")
async def schedule(interaction: discord.Interaction):
    initialize_guild_settings(interaction.guild.id)
    schedule = settings['guilds'][str(interaction.guild.id)]['roles']
    schedule_message = "**Role Schedule:**\n"
    for day, role in schedule.items():
        schedule_message += f"{day}: {role if role else 'No role assigned'}\n"
    await interaction.response.send_message(schedule_message)

# Command to display all available commands and their descriptions
@bot.tree.command(name="help", description="Displays all available commands and their usage.")
async def help_command(interaction: discord.Interaction):
    help_message = (
        "**Soundwave Bot Commands:**\n\n"
        "**/set_channel** - Set the current channel as the Soundwave channel where roles can post.\n"
        "**/set_role [day] [role]** - Assign a role to a specific day of the week.\n"
        "**/s-day** - Display whose day it is to post today.\n"
        "**/s-tomorrow** - Display whose day it will be to post tomorrow.\n"
        "**/schedule** - View the role posting schedule for this server"
        "**/help** - Display this help message with all available commands.\n"
    )
    await interaction.response.send_message(help_message)  

@bot.tree.command(name="update", description="Send an update message to all servers' Soundwave channels (bot owner only).")
async def update(interaction: discord.Interaction, message: str):
    # Check if the user is the bot owner
    if interaction.user.id != BOT_OWNER_ID:
        await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
        return

    sent_to_guilds = 0
    failed_guilds = 0

    for guild_id, guild_settings in settings['guilds'].items():
        guild = bot.get_guild(int(guild_id))
        if guild is None:
            continue  # Skip if the bot is not part of this guild anymore

        channel_id = guild_settings.get('channel_id')
        if channel_id is None:
            failed_guilds += 1
            continue  # Skip if no Soundwave channel is set for this guild

        channel = guild.get_channel(channel_id)
        if channel is None:
            failed_guilds += 1
            continue  # Skip if the channel doesn't exist anymore

        try:
            await channel.send(f"**Update from the Soundwave bot**:\n{message}")
            sent_to_guilds += 1
        except discord.Forbidden:
            failed_guilds += 1  # If the bot doesn't have permissions in the channel

    await interaction.response.send_message(
        f"Update sent to {sent_to_guilds} servers. Failed to send to {failed_guilds} servers.", ephemeral=True
    )


# Function to check permissions and update roles
async def check_permissions():
    now = datetime.utcnow()
    current_day = now.strftime("%A")

    for guild_id, guild_settings in settings['guilds'].items():
        guild = bot.get_guild(int(guild_id))
        if guild is None or guild_settings['channel_id'] is None:
            continue

        channel = guild.get_channel(guild_settings['channel_id'])
        if channel is None:
            continue

        # Get the role that should have permissions today
        role_name = guild_settings['roles'].get(current_day)
        role = discord.utils.get(guild.roles, name=role_name)

        # Update channel permissions
        for day, role_name in guild_settings['roles'].items():
            role_to_modify = discord.utils.get(guild.roles, name=role_name)
            if role_to_modify:
                send_messages_perm = (day == current_day)

                await channel.set_permissions(role_to_modify,
                                        send_messages = send_messages_perm,
                                        attach_files = send_messages_perm,
                                        embed_links = send_messages_perm,
                                        create_polls = send_messages_perm,
                                        send_voice_messages = send_messages_perm)

# Schedule the task to run every hour
@tasks.loop(hours=1)
async def scheduled_task():
    await check_permissions()


#Waiter for full hour 
async def wait_until_next_hour():
    now = datetime.now()

    minutes_remaining = 60 -now.minute

    seconds_remaining =  (minutes_remaining * 60) - now.second
    print(f"Waiting {seconds_remaining}")
    await asyncio.sleep(seconds_remaining)

    print(f"Its the next hour.. Running")


# Start the scheduled task
@scheduled_task.before_loop
async def before_scheduled_task():
    await bot.wait_until_ready()
    await wait_until_next_hour()
  
# Event that triggers when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    await bot.tree.sync()  # Sync the slash commands
    print('Slash commands synced!')
    await check_permissions()
    scheduled_task.start()  # Start the scheduled task for permission checks

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)

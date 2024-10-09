<h1 align=center> Soudwave-Bot </h1>

**Soundwave Bot** is a Discord bot designed to automate role-based permissions for posting on specific days. Each day, the bot assigns permissions to a designated role, allowing only users with that role to post, attach files, send voice messages, and embed links in a specific channel.


<h1 align=center> Features </h2> 

- **Role Assignment by Day**: Each day of the week can have a different role assigned to post in the designated channel.
- **Automatic Permission Updates**: The bot automatically updates channel permissions at the start of each day, enabling only the assigned role to post and share content in the configured channel.
- **Command-Based Configuration**: Users with the appropriate permissions can use slash commands to configure the bot and check who can post on a given day.
- **Hourly Permission Check**: The bot checks and updates permissions every hour, ensuring proper role management throughout the day.

<h1 align=center >Commands </h1>

<p align="center">
1. <strong>Set_channel</strong>
   <br>
   - Sets the current channel as the "Soundwave" channel where the daily role will have posting permissions.
   <br>
   - Example: <code>/set_channel</code>
</p>
<p align="center">
2. <strong>Set_role [day] [role]</strong>
   <br>
   - Assigns a specific role to a given day of the week. Only users with the "Soundwave Role" can use this command.
   <br>
   - Example: <code>/set_role Monday @MyRole</code>
</p>

<p align="center">   
3. <strong>S-day</strong>
   <br>
   - Displays which role is assigned to post today.
   <br>
   - Example: <code>/whose_day</code>
</p>

<p align="center">
4. <strong>S-tomorrow</strong>
   <br>
   - Shows the role assigned to post tomorrow.
   <br>
   - Example: <code>/whose_day_tomorrow</code>
</p>

<p align="center">
5. <strong>Schedule</strong>
   <br>
   - Displays the posting schedule for the entire week.
   <br>
   - Example: <code>/schedule</code>
</p>

<p align="center"> 
6. <strong>Help</strong>
   <br>
   - Displays a list of all available commands with descriptions.
   <br>
   - Example: <code>/help</code>
</p>

<p align="center">
7. <strong>Update [message]</strong> (Bot owner only)
   <br>
   - Sends an update message to all servers' "Soundwave" channels.
   <br>
   - Example: <code>/update "Here’s an update from the bot!"</code>
   </p>


<h1 align=center>Add the Bot to Your Server</h1>
<p align=center>
If you want to use the bot you can invite it you your server with this link:
<a href="https://discord.com/oauth2/authorize?client_id=1289690644310392884&permissions=268437520&integration_type=0&scope=bot
">Add Bot</a>
</p>


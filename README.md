<h1 align=center> Soudwave-Bot </h1>

**Soundwave Bot** is a Discord bot designed to automate role-based permissions for posting on specific days. Each day, the bot assigns permissions to a designated role, allowing only users with that role to post, attach files, send voice messages, and embed links in a specific channel.


<h1 align=center> Features </h2>

- **Role Assignment by Day**: Each day of the week can have a different role assigned to post in the designated channel.
- **Automatic Permission Updates**: The bot automatically updates channel permissions at the start of each day, enabling only the assigned role to post and share content in the configured channel.
- **Command-Based Configuration**: Users with the appropriate permissions can use slash commands to configure the bot and check who can post on a given day.
- **Hourly Permission Check**: The bot checks and updates permissions every hour, ensuring proper role management throughout the day.

## Commands

1. **Set_channel**
   - Sets the current channel as the "Soundwave" channel where the daily role will have posting permissions.
   - Example: `/set_channel`
   
2. **Set_role [day] [role]**
   - Assigns a specific role to a given day of the week. Only users with the "Soundwave Role" can use this command.
   - Example: `/set_role Monday @MyRole`
   
3. **S-day**
   - Displays which role is assigned to post today.
   - Example: `/whose_day`
   
4. **S-tomorrow**
   - Shows the role assigned to post tomorrow.
   - Example: `/whose_day_tomorrow`
   
5. **Schedule**
   - Displays the posting schedule for the entire week.
   - Example: `/schedule`
   
6. **Help**
   - Displays a list of all available commands with descriptions.
   - Example: `/help`
   
7. **Update [message]** (Bot owner only)
   - Sends an update message to all servers' "Soundwave" channels.
   - Example: `/update "Here’s an update from the bot!"`
<h1 align=center>Set-Up</h1>

<a href="[url](https://discord.com/oauth2/authorize?client_id=1289690644310392884&permissions=268437520&integration_type=0&scope=bot
)">link text</a>


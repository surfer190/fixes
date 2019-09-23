# Running a node app in production

_I don't know much about js, I also don't like it_

Usually you can run your app in `dev` mode with:

    node app.js

In production however you want to use Nginx to serve static files and a process manager to handle serving your app

Install pm2

    sudo npm install -g pm2

Start the app with pm2 (can use `-i max` for cluster mode)

    pm2 start app.js

This will start your app in the background

Now make a systemd entry for the app with:

    pm2 startup systemd

Ensure to run the result of the above command

then:

    pm2 save

Now stop the manual process:

    pm2 kill

and start the systemd file:

    sudo systemctl start pm2-<user>

Also set up the nginx reverse proxy for the port your app is running on from the link below

## Sources

* [How to Set up and Deploy a Node.js/Express Application for Production](https://deploybot.com/blog/guest-post-how-to-set-up-and-deploy-nodejs-express-application-for-production)
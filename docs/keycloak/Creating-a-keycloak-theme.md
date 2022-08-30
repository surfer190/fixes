---
author: ''
category: Keycloak
date: '2020-05-19'
summary: ''
title: Creating A Keycloak Theme
---
## Creating a Keycloak Theme

1. Mount a local theme to the container (assuming keycloak already running)

    # Create directory for the theme
    mkdir my-theme

    docker container list
    docker commit <running-container-id> <commit-name>
    docker run -d -p 5000:8080 --mount type=bind,source=<my-source>,target=<my-target> <commit-name>

2. Disable Cache

    The original values are:

        <staticMaxAge>2592000</staticMaxAge>
        <cacheThemes>true</cacheThemes>
        <cacheTemplates>true</cacheTemplates>

    Set it to:

        <staticMaxAge>-1</staticMaxAge>
        <cacheThemes>false</cacheThemes>
        <cacheTemplates>false</cacheTemplates>

    Copy the file to the host:

        docker cp <container>:opt/jboss/keycloak/standalone/configuration/standalone.xml .

    Send  back with:

        docker cp standalone.xml <container>:/opt/jboss/keycloak/standalone/configuration/standalone.xml

3. Make the login theme

        cd <my-theme>
        mkdir login
        cd login
        vi theme.properties

    Add the following:

        parent=base
        import=common/keycloak

    Then go to login. Then change `parent=keycloak` and it _should_ change.

    For me I had to restart the keycloak service.

4. Add CSS

    add the file `themes/mytheme/login/resources/css/styles.css`

        .login-pf body {
            background: DimGrey none;
        }

    then edit `theme.properties`:

        styles=css/styles.css

    > This removes overrides all the styles of the parent. So you can add them again with: `node_modules/patternfly/dist/css/patternfly.css node_modules/patternfly/dist/css/patternfly-additions.css lib/zocial/zocial.css css/login.css css/styles.css`

5. Add Images

    Add to `themes/mytheme/login/resources/img`

    You can then use the image with:

        body {
            background-image: url('../img/image.jpg');
            background-size: cover;
        }

    or:

        <img src="${url.resourcesPath}/img/image.jpg">


### Sources

* [Keycloak Theme Customisation](https://www.keycloak.org/docs/latest/server_development/index.html#theme-types)
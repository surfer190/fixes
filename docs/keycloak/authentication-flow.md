---
author: ''
category: Keycloak
date: '2020-02-14'
summary: ''
title: Authentication Flow
---
## Changing the Authentication Flow

1. `Configure -> Authentication`

2. Ensure the `Flows` tab is open

3. Make a copy of the flow with the `Copy` button

4. Delete the `Username and Password Form`

5. Add a new execution by clicking `Copy Of Browser Forms` -> `Actions` -> `Add Execution`

6. Set the `Provider` to `Send Reset Email`

7. Move it above `OTP Form` with the arrow buttton

8. Set it as `required`

Set the new flow for the browser with:

1. Go to the `Bindings` tab

2. Change the browser flow to the newly created flow

> Test is out

### Make COnfigu Changes to the Existing Flow

You can Change the OTP from `optional` (only required if the user has configured) to `required`.

---
author: ''
category: Django
date: '2021-12-19'
summary: ''
title: Django and HTMX
---

# Django and HTMX

## 0: The Django HTMX Stack

> In a perfect world, we would get to send and receive HTML with Django. Only updating the parts that got changed in the DOM, without reloading the whole page.

That perfect world is here. By using an HTMX/Django stack and the techniques in this course, we don't have to worry about APIs, complicated Javascript frameworks, or the limitations of reloading the page on each dynamic action. We get to have all the goodies of a SPA and Django without any of the limitations or overhead

HTMX allows:

* The first superpower is the response of the server doesn't have to replace the whole page. It can replace just the pieces of the DOM you specify.
* A user can make a request to the server with anything in the DOM. Clicking a `<div>` tag? That works. Moving their mouse over something? Sure! Typing something in an input field? Yes. We can even make a request every few seconds, without the user doing anything.

### Example Newsletter Signup

Purpose:

1. User puts in email
2. Validate email format
3. Give user feedback
4. Let the user know of update without reloading page

    <form hx-post="{% url 'email' %}" >
    <div 
    id="email_form" 
    hx-target="#email_form" 
    hx-swap="outerHTML">
        <h3>Email Form</h3>
        <label>Email Address</label>
        <input 
        name="email" 
        placeholder="Your email here..." 
        required = "required"
        >
    <button> Submit </button>
    </div>
    </form>

* `hx-post` means that when the form is submitted a `POST` is done. Also has `hx-get`, `hx-delete` and `hx-put`.
* `hx-target` means the response will only change the DOM element with that css selector
* `hx-swap` specifies how we want to change the target DOM element

The above will deal with numbers 1 and 4.

    <form hx-post="{% url 'email' %}" >
    <div
    id= "email_form" 
    hx-target="#email_form" 
    hx-swap="outerHTML">
        <h3>Email Form</h3>
        <label>Email Address</label>
        <input 
        name="email" 
        placeholder="Your email here..." 
        required = "required"
        hx-post="{% url 'custom_email_validation' %}"
        hx-trigger= "changed" 
        hx-target = "#email_feedback"
        >
        <button> Submit </button>
    </div>
    </form>
    <div id="email_feedback" > </div>

To allow for js style validation:

* Any change on the input field triggers a `POST` via `hx-trigger` to `custom_email_validation`
* It would replace the content in `email_feedback`

## 1: To Do App

> Start the basic project

Looking at:

    <!-- in components/landing_page.html -->
    <div class="container-fluid d-flex align-items-center justify-content-center" 
    style="height: 100vh;" 
    id="landing_page"> <!-- we added an id -->

    <div class= "content m-0 text-center mw-full h-full">
        <h1 class="text-primary" style="font-size:50px;"> HTMX/Django: To do App </h1> 
        <p> Keep track of what needs to be done! </p>
        <!-- we changed this button -->
        <button 
            class="btn btn-primary mt-10" 
            role="button" 
            hx-get="{% url 'account_signup' %}"
            hx-trigger="click"
            hx-target="#landing_page"
            hx-swap="outerHTML"
            hx-push-url="/signup">
            Start Your List 
            </button> 
    </div>
    </div>

1. `hx-get`: We are making a GET request to the account sign up URL (implemented for us via allauth)
2. `hx-trigger`: The request is triggered when the user clicks the button
3. `hx-target`: The component that will be swapped out. Notice, we added an ID to our landing_page component
4. `hx-swap`: How are we going to swap it. In our case, we are swapping the entire div out.
5. `hx-push-url`: This pushes a new URL to the url bar, and saves the old component to the history. Without it, the URL wouldn't change.

The parent DOM element can be used to children elements to inherit certain `hx-` attributes.

For example: For all hgtmx elements within this div...all the attributes will have the `hx-swap` and `hx-target` of the parent.

    <div class="card w-600 mw-full mx-auto" id="tasks" hx-swap= "outerHTML"
    hx-target = "#tasks">

Anytime you have a traditional `<a>` tag and want to turn it into an HTMX, simply wrap its parent element with the `hx-boost` attribute! As a bonus, `hx-boost` even works if Javascript is disabled by falling back to the normal `<a>` tag behavior.

#### SEO

Let's go ahead and see if our next user story works already by opening a private browser and copying and pasting our URL. Here is the story: "I can access the blog internally as a SPA or externally by sharing a link"

It works right? Great! That's another thing off our plate. Now, if you are a Django-first developer, this user story might seem weird to you. Of course, a link is a link, it doesn't matter if it's an internal link or coming from outside.

But I put that story intentionally because it is usually a pain point for React and Vue-first developers. When we rely exclusively on javascript to handle our routing, it does so via the browser history. This can cause some weird bugs and side effects.

### This Keyword

You can use the `this` keyword to specify the item that was actioned:

    <button 
    hx-get="play"
    hx-target="this"

    </button>




# Laravel 5.2 Changelog and What's New?

## Implicit route binding

Laravel implicitly (you don't have to explicitly type this) finds the model for you

ie. `User::findOrFail(3)`

eg.

```
Route::get('api/users/{user}', function (App\User $user) {
    return $user;
});
```

**Note**

- Only works when wildcard name `{ user }` equals `$user`
- Must match primary key otherwise you need a _custom binding_ So you need to add a route binding in `boot` method of `app/providers/routes.php`

## API Rate Limiting

```
Route::get('/api/search/{term}', function($term) {
  return [
    'results' => $term
  ];
})->middleWare('throttle:3');
```

In `throttle:x,y`, `x` is the maxAttempts and `y` is the decayMinutes

Returns a `429` Error response: `Too many attempts`

## Auth and Resets in Minutes

New artisan command `php artisan make:auth`

It is better to do this after initial project creation

`views/auth` has all the basic views

Creates typical layout: login, registration, password reset

Laravel hides all the routes in `Route::auth()` in `app/Http/routes.php`, hidden in `Illuminate.Routing.auth.php`

Remember you can always use `php artisan route:list` to check your `routes`

Auth throttling also comes out of the box

## Validating arrays

Validating a number of email addresses or a number of cellphone numbers

Use inputs with the same name. eg. `name=email[]`

```
  $validator = Validator::make($request->all(), [
    'email.*' => 'required|email'
  ]);
```

**Note** : It gets a lot mroe involved when adding error messages and returning the old values etc.

## Token based authentication

In `config.auth.php` there are some `guards`, `web` which is the standard session based authentication and now a new `api` which is **token based**

You can create your custom guard here as well

Stateless so the token is saved in the db, a temporary user is created

Create route group:

You will need to add a `api_token` column to user table migrations:

```
  $table->string('api_token', 60)->unique();
```

then refresh

`php artisan migrate:refresh`

Now the user has an api token associated with the account and give that to a third party account. They can't sign in with password, but can query.

```php
Route::group(['prefix' => 'api/v1', 'middleware' => 'auth:api'], function(){
  Route::get('users/{user}', function (App\User $user) {
      return $user;
    });

  Route::get('/', function(){
      // return Auth::user(); //won't work as it still uses the web guard
      return Auth::guard('api')->user();
    })
})
```

**Note**:

- The **auth:api** which uses the token guard
- To test as an api must simulate an ajax request with `httpie --json`
- To test with the `api_token` included in the request:

    `http localhost:8888/api/v1/users/1 api_token=3245jfbsldifuya8yf --json`

- Change the default guard in `app/config/auth.php`

#### Source

- [Laracast What's new in Laravel 5.2](https://laracasts.com/series/whats-new-in-laravel-5-2)

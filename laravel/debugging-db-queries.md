# Debugging DB Queries Lavel 5.1

Add `toSQL()` to the query.

Then debug with `dd`

    results = User::where(function($q) use ($request) {
      $q->orWhere('email', 'like', '%john@example.org%');
      $q->orWhere('first_name', 'like', '%John%');
      $q->orWhere('last_name', 'like', '%Doe%');
  })->toSql();
  dd($results);

Source: [Scotch Laravel Db Debugging Guid](https://scotch.io/tutorials/debugging-queries-in-laravel)e
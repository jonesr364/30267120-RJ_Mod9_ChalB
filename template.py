# index.html

<html>
<head>
<title>Request Example</title>
</head>
<body>
<form method="POST" action="/temperature">
City name/zip : <input type="text" name="location">
<input type="submit">
</form>
</body>
</html>


# temperature.html

<html>
<head><title>Current Temperature</title></head>
<body>
<h1> The current temperature (C) is : {{ temp }} degrees. </h1>
</body>
</html>
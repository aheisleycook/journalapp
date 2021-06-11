<!doctype html5>
<html>
<head>
<style>

html {
    width: auto;
}

header {
    clip: auto;
    background-color: black;
    color: white;
    width: 100%;
    
}



header>span {
    position:relative;
    left: 10px;
    top: -2px;
    outline: solid 1px 1px 1px 1px blue;
}
nav > li {
    display: inline;
    padding: 4px;
}

</style>
<meta charset='utf-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<title>langing</title>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<link rel='stylesheet' type='text/css' media='screen' href='main.css'>
<script src='main.js'></script>
<meta description="my post site">
</head>
<body>
<header>
<span>postboard.com</span>
<form class="postsearch" method="get" name="query" action="postboard/searchposts.php">
<input type="search">
<input type="submit">
</form>
<h3>landing page</h3>
</header>
<nav>
   <li><a href="/postboard/addform.html">addform</a></li>
   <li><a href="/postboard/deleteform.html">deletform</a></li>
   <li><a href="/">home</a></li>
</nav>
<main>
    <?php
        $conn = new mysqli('localhost', 'postboarduser', 'A714708o', 'postboard');

        $sql = 'select * from posts';
        $max = 10;
        $posts = $conn->query($sql)->result;
        $posts->fetchall();
        for ($i = 0; $i <= $max; ++$i) {
            echo $posts[i];
        }

    ?>
</main>
<footer>
    <address>
        4318 stern Ave
        91423
        postboard.com 
    </address>
</footer>
</body>
</html>
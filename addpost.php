<?php

function submitentry()
{
    $title = $_POST['title'];
    $description = $_POST['description'];
    $tags = $_POST['tags'];
    $conn = new mysqli('localhost', 'postboarduser', 'A714708o', 'postboard');
    $sql = "insert into values Posts(0,$title,$description,$tags)";
    $conn->execute($sql);
    if ($conn) {
        return $conn->connection_status;
    } else {
        $conn->mysqli_error;
    }
}

submitentry();

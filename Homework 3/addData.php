<?php
$host = "127.0.0.1";
$user = "GO";
$pass = "1234";

$databaseName = "lightdatabase";
$tableName = "lights";

$con = mysqli_connect($host, $user, $pass, $databaseName);

if ($_GET["h"] || $_GET["t"] || $_GET["l"])
{
    $humi = $_GET["h"];
    $temp = $_GET["t"];
    $light = $_GET["l"];

    $sql = "insert into $tableName (humi, temp, status) VALUES (" . $humi . "," . $temp . "," . $light . ")";
    $result = mysqli_query($con, $sql);
}
?>

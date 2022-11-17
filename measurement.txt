<?php
$servername = "172.20.241.9";
$username = "dbaccess_rw";
$password = "fasdjkf2389vw2c3k234vk2f3";
$dbname = "measurements";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
        }

$sql = "SELECT  id, groupid, sensorvalue_a, sensorvalue_b, sensorvalue_c, sensorvalue_d, sensorvalue_e, sensorvalue_f FROM rawdata WHERE groupid=77 ORDER BY id DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
   while($row = $result->fetch_assoc()) {
      echo "Sender ip:" . $row["groupid"] . " - Sensor value | X: " . $row["sensorvalue_a"] . " | Y: " . $row["sensorvalue_b"] . " | Z: " . $row["sensorvalue_c"] . "   | Position ID: " . $row["sensorvalue_e"] . "  ID : " . $row["sensorvalue_d"] . "<br>" ;
   }
}

$conn->close();
?>

<?php
$enlace = mysqli_connect("localhost", "rentcoac_adsteam", "LlB7Rq1CMP]z", "rentcoac_ads");

if (!$enlace) {
    echo "Error: No se pudo conectar a MySQL." . PHP_EOL;
    echo "error de depuración: " . mysqli_connect_errno() . PHP_EOL;
    echo "error de depuración: " . mysqli_connect_error() . PHP_EOL;
    exit;
}
?>
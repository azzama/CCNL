<?php
// allow CORS, otherwise it will complain
header("Access-Control-Allow-Origin: *");
// This function is from https://stackoverflow.com/a/48882693/7889212
function getIP($ip = null, $deep_detect = TRUE){
if (filter_var($ip, FILTER_VALIDATE_IP) === FALSE) {
$ip = $_SERVER["REMOTE_ADDR"];
if ($deep_detect) {
if (filter_var(@$_SERVER['HTTP_X_FORWARDED_FOR'], FILTER_VALIDATE_IP))
$ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
if (filter_var(@$_SERVER['HTTP_CLIENT_IP'], FILTER_VALIDATE_IP))
$ip = $_SERVER['HTTP_CLIENT_IP'];
}
} else {
$ip = $_SERVER["REMOTE_ADDR"];
}
return $ip;
}
// receive POST
$API = $_POST["API"];
$IP = getIP();
// create curl resource
$ch = curl_init();
// set API key header
$headers = array( 'X-Key: ' . $API );
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
// set url
curl_setopt($ch, CURLOPT_URL, "http://v2.api.iphub.info/ip/".$IP);
//return the transfer as a string
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
// $output contains the output string
$output = curl_exec($ch);
echo $output;
// close curl
curl_close($ch);
?>
<?php
$to = "voxzee@hexcode.tk";
$subject = "Impressions";
$txt = "report issue";
$headers = "From: sender" . "\r\n" .
"CC: harsh.vox20@gmail.com";

mail($to,$subject,$txt,$headers);
?>
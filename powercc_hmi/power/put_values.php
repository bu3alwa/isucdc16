<?php

$systems = array(
    "gen1_breaker" => "gen1_breaker",
    "gen1_generation" => "gen1_generation",
    "relay1_breaker" => "relay1_breaker",
    "gen2_breaker" => "gen2_breaker",
    "gen2_generation" => "gen2_generation",
    "relay2_breaker" => "relay2_breaker"
)


$var = $_GET['var'];
$value = $_GET['value'];

$sys = $systems[$var];
$val = int($value);


exec("python py-bin/opc_put_values.py ".$sys." ".$val." 2>&1", $output, $return_var);

?>

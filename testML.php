<?php
$input = "0,1,2";

// Command to execute Python script with input
$command = 'echo ' . $input . ' | python run.py';

// Execute command using exec()
exec($command, $output, $return_var);

//convert output array[0] to string and remove bracket
$output = implode($output);

// Print the output of the command
echo ($output[1]);

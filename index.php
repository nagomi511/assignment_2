<?php
$a = $_GET['a'] ?? null;
$b = $_GET['b'] ?? null;
$c = $_GET['c'] ?? null;

if ($a === null || $b === null || $c === null) {
    echo '<form>
            a: <input name="a"><br>
            b: <input name="b"><br>
            c: <input name="c"><br>
            <button type="submit">Calculate</button>
          </form>';
    exit;
}

$cmd = "/usr/bin/python3 /var/www/html/calculate.py $a $b $c";
$output = shell_exec($cmd);
echo $output;
?>


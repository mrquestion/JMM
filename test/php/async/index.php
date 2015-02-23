<?
error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);
ini_set("display_errors", 1);
date_default_timezone_set("Etc/GMT+9");

function logs() {
	echo "<pre style=\"font-family:Consolas\">";
	$args = func_get_args();
	foreach ($args as $o) {
		var_dump($o);
	}
	echo "</pre>";
}

$a = trim($_POST['a']);
$b = trim($_POST['p']);
$c = trim($_POST['u']);

$p = new PDO("mysql:host=localhost;dbname=jmm", "jmm", "jmm");
$p->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
$p->exec("SET AUTOCOMMIT = FALSE");
?>
<?
$p->beginTransaction();
?>
<?
$result = "false";
if (strlen($a) > 0 && strlen($b) == 64) {
	$b = hash("sha256", $b);
	$s = sprintf("SELECT i FROM mach WHERE a = '%s' and p = '%s'", $a, $b);
	$rs = $p->query($s)->fetch();
	if ($rs) {
		$mi = $rs['i'];
		$ai = 1;
		$s = sprintf("SELECT ifnull(max(e), 0) as e FROM sub WHERE ai = %d and mi = %d", $ai, $mi);
		$rs = $p->query($s)->fetch();
		if ($rs) {
			$e = $rs['e'];
			if ($e < 10) {
				$s = sprintf("INSERT INTO sub(ai, mi, e, u) VALUES(%d, %d, %d, '%s')", $ai, $mi, $e + 1, $c);
				$p->query($s);
				$result = "true";
			}
		}
	}
}
?>
<?=$result?>
<?
$p->commit();
$p = null;
?>
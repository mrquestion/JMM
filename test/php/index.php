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

$p = new PDO("mysql:host=localhost;dbname=jmm", "jmm", "jmm");
$p->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
$p->exec("SET AUTOCOMMIT = FALSE");
?>
<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8" />
<title>JMM :: made by R</title>
<style>
</style>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1/jquery-ui.min.js"></script>
<script>
</script>
</head><body>
<?
$p->beginTransaction();
?>
<h1>JMM</h1>
<h2>Tables</h2>
<?
function table_dump($p, $s) {
	return $p->query(sprintf("SELECT * FROM %s", $s))->fetchAll();
}
function print_table_dump($p, $s) {
	$t = table_dump($p, $s);
	$h = array();
	array_push($h, sprintf("<h3>- %s</h3>", $s));
	array_push($h, '<table border="1" width="800" style="font-size:10px">');
	$f = true;
	foreach ($t as $r) {
		if ($f) {
			array_push($h, "<tr>");
			foreach ($r as $k => $v) {
				array_push($h, sprintf("<th>%s</th>", $k));
			}
			array_push($h, "</tr>\n");
			$f = false;
		}
		array_push($h, "<tr>");
		foreach ($r as $k => $v) {
			array_push($h, sprintf("<td>%s</td>", $v));
		}
		array_push($h, "</tr>\n");
	}
	array_push($h, "</table>");
	$s = join('', $h);
	print($s);
}
print_table_dump($p, "ani");
print_table_dump($p, "mach");
print_table_dump($p, "sub");
?>
<h2>Test</h2>
<?

$s = "SELECT i, n, w, t FROM ani ORDER BY w";
$rs = $p->query($s)->fetchAll();
$dotw = array("일" => array(), "월" => array(), "화" => array(), "수" => array(), "목" => array(), "금" => array(), "토" => array());
$dotws = array("일", "월", "화", "수", "목", "금", "토");
foreach ($rs as $r) {
	array_push($dotw[$dotws[$r['w']]], $r);
}
$s = "SELECT mi FROM sub GROUP BY mi";
$rs = $p->query($s)->fetchAll();
$machs = array();
foreach ($rs as $r) {
	$s = sprintf("SELECT n FROM mach WHERE i = %d", $r["mi"]);
	$machs[$r["mi"]] = $p->query($s)->fetch()['n'];
}
?>
<ol><? foreach ($dotw as $k => $v) { ?>
	<li>
		<div><?=$k?></div>
		<ul><? foreach ($v as $r) { ?>
			<li><? $m = null; preg_match("/[0-9]{4}-[0-9]{2}-[0-9]{2} ([0-9]{2}):([0-9]{2}):[0-9]{2}/", $r['t'], $m); ?>
				<div>[<?=$m[1]?><?=$m[2]?>] <?=$r['n']?></div>
				<?
				//$s = sprintf("SELECT a.mi, a.e, a.u FROM sub as a, (SELECT mi FROM sub where ai = %d GROUP BY mi) as b WHERE a.mi = b.mi and a.e = (SELECT max(e) FROM sub WHERE mi = b.mi) and a.ai = %d", $r['i'], $r['i']);
				//$s = sprintf("SELECT mi, e, u FROM sub WHERE ai = %d ORDER BY e DESC", $r['i']);
				$s = sprintf("SELECT mi, e, u FROM sub WHERE (ai, mi, e) IN (SELECT ai, mi, max(e) as e FROM sub WHERE ai = %d GROUP BY ai, mi)", $r['i']);
				$rs = $p->query($s)->fetchAll();
				?>
				<ul><? foreach ($rs as $r) { ?>
					<li><a href="<?=$r['u']?>" target="_blank"><?=$machs[$r["mi"]]?> <?=$r['e']?>화</a></li>
				<? } ?>
				<?/*<li><a href="<?=$rs['u']?>" target="_blank"><?=$machs[$rs["mi"]]?> <?=$rs['e']?>화</a></li>*/?>
				</ul>
			</li>
		<? } ?></ul>
	</li>
<? } ?></ol>
</body></html>
<?
$p->commit();
$p = null;
?>
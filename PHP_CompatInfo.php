#!/usr/bin/php
<?php
/**
 * Get the Compatibility info from PHP CLI
 *
 * @version    $Id$
 * @author     Davey Shafik <davey@php.net>
 * @package    PHP_CompatInfo
 * @access     public
 * @ignore
 */

ini_set('memory_limit', '24M');

require_once 'PHP/CompatInfo/Cli.php';

$cli = new PHP_CompatInfo_Cli();
$cli->run();

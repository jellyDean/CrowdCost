<?php
/**
 * The base configurations of the WordPress.
 *
 * This file has the following configurations: MySQL settings, Table Prefix,
 * Secret Keys, WordPress Language, and ABSPATH. You can find more information
 * by visiting {@link http://codex.wordpress.org/Editing_wp-config.php Editing
 * wp-config.php} Codex page. You can get the MySQL settings from your web host.
 *
 * This file is used by the wp-config.php creation script during the
 * installation. You don't have to use the web site, you can just copy this file
 * to "wp-config.php" and fill in the values.
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'bitnami_wordpress');

/** MySQL database username */
define('DB_USER', 'bn_wordpress');

/** MySQL database password */
define('DB_PASSWORD', '35c813cb2c');

/** MySQL hostname */
define('DB_HOST', 'localhost:3306');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY', 'bb1ddef13c87e5deb53552348455daa10a6d0b53e8c7da4bb88e32750672c7d9');
define('SECURE_AUTH_KEY', 'eafc9d094cc0f2529aada361f9e42899d94ae818c9073b939b2bd8d319d7e71d');
define('LOGGED_IN_KEY', '2bb96c1d29deab7cbd4aec2a467164dd03755834095ba0b112af92ad4adba4e6');
define('NONCE_KEY', '37d51c47fe3ba59a7cb6c19145e8a46cef8667af6687ed2dc863880f0d3174ca');
define('AUTH_SALT', 'fa8318436c455d0c57500963992f65d8ccf07bf16bc7554e24e695c78b092ad3');
define('SECURE_AUTH_SALT', '105d7bd0e3a65ea99d63bc651c9eef528b4d3a9186a966cc147d07b96fbbe4ad');
define('LOGGED_IN_SALT', 'bd4a29a272451f84686d96248ed08a35903b45050ff631dc5fa955d5c5aab914');
define('NONCE_SALT', 'f276d86ee95f380ca3c8bfd5c924094b622c2a48624a5977355a3be982280642');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each a unique
 * prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */
/**
 * The WP_SITEURL and WP_HOME options are configured to access from any hostname or IP address.
 * If you want to access only from an specific domain, you can modify them. For example:
 *  define('WP_HOME','http://example.com');
 *  define('WP_SITEURL','http://example.com');
 *
*/

define('WP_SITEURL', 'http://' . $_SERVER['HTTP_HOST'] . '/');
define('WP_HOME', 'http://' . $_SERVER['HTTP_HOST'] . '/');


/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');

define('WP_TEMP_DIR', '/opt/bitnami/apps/wordpress/tmp');


define('FS_METHOD', 'ftpext');
define('FTP_BASE', '/opt/bitnami/apps/wordpress/htdocs/');
define('FTP_USER', 'bitnamiftp');
define('FTP_PASS', 'Kafo0xN1uXLwALHudIHKin0KZm0chO9nwg3hBK85cRMb4qdL0N');
define('FTP_HOST', '127.0.0.1');
define('FTP_SSL', false);


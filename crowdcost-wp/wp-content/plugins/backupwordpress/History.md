
n.n.n / 2015-02-24
==================

  * Merge pull request #728 from humanmade/issue-728
  * Merge pull request #739 from humanmade/upgrade-options
  * Bump version
  * strtolower is redundant
  * Upgrade routine
  * Use the Service name as the setting name
  * Cleear settings for schedule settings
  * Fixes bug in displaying settings error notices
  * Update version number
  * Merge pull request #726 from humanmade/fix-fatal-error-missing-class-addons
  * Leave bare minimum to avoid fatal error
  * remove old main plugin class
  * remove deprecated notice
  * Throw a deprecated warning
  * Add BWP class
  * Bump version
  * Introduces a deprecated.php file

n.n.n / 2015-02-03
==================

  * Merge pull request #687 from humanmade/fixup-setup-class
  * Merge pull request #724 from humanmade/simplify-bwp-file-timestamp
  * Simplify the file name timestamp
  * Fix class file name
  * Merge pull request #723 from humanmade/willmot-slack-notifications
  * Add missing transients to uninstall routine
  * switch Travis notifications to Slack instead of Hipchat
  * Do not delete backups on uninstall
  * wrap in parenthesis
  * Fix include paths after moving uninstall to own file herpderp
  * Update BackUp class include
  * Merge branch 'master' into fixup-setup-class
  * Merge pull request #719 from humanmade/iis-fixes
  * Merge pull request #720 from humanmade/refactor-fixes
  * Add all cases to switch
  * Pass scanned files sizes through conform_dir()
  * Fix some classes and requires
  * Merge branch 'master' into fixup-setup-class
  * Merge branch 'master' into fixup-setup-class
  * Merge pull request #684 from humanmade/issue-684
  * Fix namespaces
  * Remove unnecessary wildcard from regex
  * Merge branch 'master' into issue-684
  * Merge pull request #667 from humanmade/crazy-refactor
  * Remove some duplication
  * Formatting
  * Fix Class name
  * Merge branch 'master' into crazy-refactor
  * Blank line
  * Uses a DirectoryIterator to delete files
  * Merge pull request #683 from humanmade/change-singleton-implementation
  * Merge branch 'master' into crazy-refactor
  * Remove tests for now
  * Fix stable tag number
  * Revert to using uninstall.php
  * Add tests for uninstall and deactivate
  * Remove double lie break
  * Remove double line break
  * Remove phpdocumentor
  * We still need to require some scripts...
  * We dont need to check for this constant in the hook callback
  * Use get_col to directly have an array of schedule option names
  * Remove namespacing
  * Remove debugging
  * Make the uninstall, activation and deactivation hooks work
  * Change the singleton implementation to not use the static() function
  * Merge pull request #682 from duritong/fix_path_argument
  * path argument interfers with wp-cli path argument.
  * Fix some scrutinizer issues, mostly major ones
  * Consistent default name for database dumps
  * Major 5.3 re-factoring fun
  * Merge hm-backup into backupwordpress
  * Minor code formatting
  * else if should be elseif
  * Update the WP_CLI command to fix some issues
  * Add support for copying and updating an existing backups
b3ffe16 (HEAD, origin/master, master) Merge pull request #670 from humanmade/fix-668
ad7e0fa Correct $response1 variable
89c87e8 (tag: 3.1-alpha) Merge pull request #475 from humanmade/issue-475
d0e6d0c Merge pull request #652 from humanmade/issue-652
804c472 (origin/issue-652, issue-652) Suppress warnings from filesystem functions
9861f06 Remove debugging function
6601346 Merge branch 'master' into issue-652
65808bb (origin/issue-475, issue-475) Fix a French string
ca35ba3 Format the intercom data better
c8cd859 Load Intercom in the admin footer
34c3af0 Fix some HTML issues
b896803 Fix tests
4c3fade Add a function that returns a given option value
071a23a Return Unknown if no average exists or invalid
4e6ca12 Add a start parameter to function
6d8047a Pass in the start time as a parameter
0410b01 Add some unit tests
740583a Make strings translatable
9861f70 Escape values
61a0441 Adds a function to track backup duration and anpther to display it
adb7b8a Adds Average Backup Duration Info
e9a4088 Improve display of arrays
1ee8c69 Fixes open_basedir warnings
8de17c3 Replace spaces with tabs for indentation
082a038 Merge pull request #664 from humanmade/wp-cron-test-improvements
cc8e46e (wp-cron-test-improvements) Improve the reliability of the wp-cron test
8bf18c5 Merge pull request #639 from humanmade/issue-639
5ad724e Merge pull request #588 from humanmade/issue-588
b87396b (issue-639) Do not start schedule if backups are not possible
069553b (origin/issue-588, issue-588) Merge branch 'master' into issue-588
876b955 Pop in the directory sizes
f6d99f6 No need to return the whole array
81fc305 Merge pull request #640 from humanmade/issue-640
c11b1b5 Merge pull request #605 from humanmade/issue-605
809528e Adapt heartbeat pulse
bdb1142 Update Javascript
0f4f758 A few adjustments based on peer review feedback.
315ff75 Update constant name
195189b Load the default translations so that activation error message is in user language
cb6fbe5 Fix a few translatable strings
8c52f3a Update French translations
2f1a3a5 Re-uglify Intercom js
727579e Use provided callback argument to determine current screen
036998c remove deprecated code
34cfdc9 Merge branch 'master' into issue-605
6951b7e Merge pull request #612 from humanmade/hmbkp-path
5c48e64 Remove PHPDoc build process
f3e9fc3 Merge branch 'master' into hmbkp-path
6457232 Merge branch 'master' into issue-605
c134e41 Ignore IDE project files
c127848 Merge pull request #651 from humanmade/remove_memory_limit_define
16213e9 Only show notices on BWP admin page
4945ce9 Merge pull request #649 from humanmade/improved_notices
b2a228c Fix class name
3ffb704 Formating
d128ae5 Make function public for now
a491cfc Get an instance of BWP to load functions
45af4c4 Fix conditional
9675432 Fix conditional
6769d23 Show admin notice if fails to meet requirements
bd56ea0 Remove unneeded function
7d7b515 Fix references
b4a9a0e Refactor main class after addition of the Setup class
0e6febe Introduce a setup class
26cb5ab Update tests
8cc3a85 Determine if we need to run a cleanup routine
71fca9c Introduce a custom hook for addons
ca5fbc7 Refactor main plugin file into a singleton class
bf5be41 Bring activation and deactivation into main plugin class
ae82d2c Ignore IDE project files
5cf0843 Merge pull request #648 from humanmade/issue-648-sprtbtnfix
93cc9ce css changes to fix support button alignment
0165a6c Merge pull request #644 from humanmade/issue-644
ea4854b Merge pull request #650 from humanmade/fix_nojs_backup
46d3601 Merge pull request #642 from humanmade/fix-missing-i18n
2fa87b0 Merge branch 'master' into hmbkp-path
bdada67 Fixes issue preventing backups from running without JS
b901112 Remove back compat memory limit define
b3fb80e Refactot HMBKP_Notices to support non-persistant notices
e9cac5f Minor refactor for PHP minimum requirements notice
65b89ff Clear previous backup notices when running a new backup
25ce583 Fix issues with custom paths
eaf520b Fixup some issues in merge_existing_paths
ca6b691 Improved singleton pattern
f679be5 Display errors in network admin
b30722e Change to text input so multiple email address are supported
6100176 Removes HTML tag from string
fe62548 Merge pull request #643 from humanmade/fix-conditional
9743f32 code is of type string
d4e8765 Remove unneeded code
070dd9e Account for new schedule
27f9e77 Make upsell sentence translatable
97aa688 Regenerate minified
6bb46f7 Fix a few linting issue
2b1ef2d Extract to a function
6401221 JSHint config
0bf6248 fix return type
d5170dd Return true if transient exists
6a0a704 Check if constant is defined
198f40a Request the site size fvia heartbeat send
b4ee172 Pass site size through heartbeat
4155280 Only calculate if necessary
939ccdb Remove phpunit and naming checks
c2a199e (tag: v3.0.4) Remove naming checks as we do this with phpcs
8cc1f65 Bump version to 3.0.4
65f5095 Don't run phpunit on Scrutinizer
e5bc0dc Merge pull request #624 from humanmade/issue-624
95873c5 Merge pull request #629 from humanmade/issue-629
fc495bd Merge pull request #633 from humanmade/fix-help-tabs-display
823107e Merge pull request #634 from humanmade/issue-634
6eece13 Merge pull request #636 from humanmade/fix-admin-scripts
7a56b46 Only build docs on master
868ae6b Wait for tests
42838dc Try using a hardcoded string
6ab00bc Simplify the backup count display
6b4684e Enqueue scripts properly
17b0610 Change how we check directory_sizes
31baca0 Disable php_cpd
7b9f9cb Merge branch 'master' into fix-help-tabs-display
1e01d21 Fix typo
d98e143 Merge branch 'master' into issue-629
5438c20 Add BackUpWordPress test case class
b03582c Move class to separate file
2102a88 Account for various testing environments
2c1469a Use HTTPS in tests setup
0766c37 Add required functions
8b9a4d8 Remove deprecated property
20bf107 Simplify writing status to file and throw Exception on failure
48d45e2 Spacing
710fbc0 Group help tab display functions
8ad56ee Remove deprecated function
9358318 call hmbkp_path directly
0f96866 Merge pull request #628 from humanmade/wpml-compat
b27e2f2 expected actual
23d3e78 Update POT file
cca1f0b Make strings ready for translation
0d0f270 Run test suites separately
69812bb Reorganize tests
43d20c4 Get the singleton instead of instantiating
b3aa187 Do not delete backups folder between tests
a771a02 Expected then Actual
e52bb77 Fix order of arguments in assertions
50fe291 No need for this var
a8a8659 Add BackUpWordPress test case class
dcbac12 Move class to separate file
4e88297 Account for various testing environments
c1e3158 Use HTTPS in tests setup
b9ce28c Merge branch 'master' into hmbkp-path
1e093b6 Update dependencies in composer.lock
40faa7c (tag: v3.0.3) Fix code coverage config
486d6c7 Fix code coverage config
04e4d9d Fix class name
889572d Merge branch 'master' into hmbkp-path
748f132 Remove asterisk from pattern
d91cfe7 Fix asterisk
a5d6af5 Rename translation files
d67f3d6 Bump plugin version to 3.0.3
4bdb26f bump version
3e3aa0d refresh readme
0e15823 Regenerate readme
40d72ce Refresh POT file
5afe400 Latest hm backup
c81b561 Merge pull request #621 from humanmade/fix-time-dependent-tests
e96e73b Merge branch 'master' into hmbkp-path
91ed195 Merge pull request #623 from humanmade/issue-623
11dcfa0 Merge pull request #620 from humanmade/issue-620
07bcd59 Merge branch 'master' into hmbkp-path
6702908 Merge pull request #597 from humanmade/issue-597
69daeef Add French translations
4396c41 Update textdomain
abd3585 Fix deleted function
1bdf3ff Use HM_Backup function to determine if shell_exec is enabled
d0c7d70 Merge branch 'master' into issue-620
b894d52 Check if file is readable first
025c581 Fix how we kick off Task
be92693 Merge pull request #625 from humanmade/issue-625
1bc3eb7 Remove unused var
db0ec01 Call recursive filescanner on admin page load
99cbe70 Update package.json
804d727 Update the POT file task params
f10bf82 Replace hmbkp with backupwordpress as textdomain
80aae82 Exclude folders
a490f77 Add Grunt task options
c73afab Checkout hmbkp-path branch
9d163c1 Make function public
32e7b12 Merge branch 'master' into hmbkp-path
32a36a4 Comments and formatting
af7c0c3 Fix scrutinizer issues
909332a Remove hard line returns
c603734 Display placeholder if exec fails
9869c23 Add 30 second time diff allowance
845b9fe Use $TRAVIS_BUILD_DIR
d163ee6 we do this in travis.yml
9e4fda4 Regenerate github account info
5722e0c Update command to reflect function rename
bcc100e Update tests to reflect function name change
1853d7b Rename function
1fe371a Filter tests to run
6892c2c Fix group flags
8b1f65c Return true on success, false on failure
012866b Unit tests php ini configs
960d5b0 Add unit tests for hmbkp_is_function_available
dddd1f8 Check if exec is available before using it
aaf06c1 Introduce a function to determine if a function was disabled in the PHP config
d3ac584 Merge branch 'master' into issue-597
225aea9 (tag: v3.0.2, origin/gh-pages) Merge pull request #610 from humanmade/phpdocs
bee261b (phpdocs) Change composer flags
6b354f1 Need to call bash to run script
b69921c Display debug info
f3e0391 Merge branch 'master' into phpdocs
14a67f2 Ignore PHP Docs and Vendor during build
dd37733 Rename hmbkp pot file
a223cc1 Changelog
128e6ab  Update readme
5c8308c Update translatable strings
a9a30d0 Regenerate CSS
01fd58a Bump version
4cc2f99 Add github user info
f43e036 Regenerate encrypted notification key for Hipchat
245b460 Regenerate composer lock file
aeeb8b2 Merge branch 'master' into phpdocs
14912a5 Merge pull request #600 from humanmade/issue-600
e8f2993 Merge pull request #347 from humanmade/issue-347
5d89edd Calculate site size on page load
f45f1ab Pull out logic into own function
bdc0572 Add parenthesis to require_once
d8158a9 Remove disk space info
a358977 Merge branch 'master' into issue-347
ea2687e Merge pull request #614 from humanmade/remove-custom-webhook
9483558 Merge branch 'master' into remove-custom-webhook
621e73b Merge branch 'master' into issue-600
54eda33 Merge pull request #611 from humanmade/fix_unit_tests
aae1791 Attempt to fix build
431df76 Merge branch 'master' into fix_unit_tests
7ae6772 define WP_TESTS_DIR
bca3838 Make sure current_action fnction is loaded
e004fe0 Remove extra slashes and semicolons
4f35f2a Use Travis env var
5126fb4 Last try
8bd5d53 Try Travis var unquoted sigh
4145a4a Actually load the HMBKP_Path class
4e32368 Merge branch 'master' into hmbkp-path
16fb29c Remove the custom webhook service
a595864 Better default WP_TESTS_DIR
c6583bd move trailingslash calls out of the loop for performance
272d663 Stop excluding duplicate backup directories
b4de446 Update wp-cli to use hmbkp_path
0286823 Introduce a HMBKP_Path class to replace hmbkp_path();
56b7aee Minor code cleanup
aeabc8c Merge pull request #599 from humanmade/issue-599
b816d56 Correct path for hm-backup so it's tests are run
ac40ab7 try this
4ac18e0 other syntax
db7873f Try just a subfolder
0ab3771 try another thing
ca4dfed test
7a35636 debugging travis
563e16d Try using travis var
c702657 Warp var in quotes
27833f0 Fix invalid command
00db4f7 Use env var
cd4042f Add list of ignored folders
6c6348a Update composer lock file
064653f Set required version to dev-master
c99feb1 Fix deprecated call
5cef443 Don't test PHP 5.2
36279c1 Rename script
4bb9cea Install composer requirements
d29dc96 add composer.lock
e707f13 Use scrutinizer code coverage
02c1cd6 Merge pull request #609 from waffle-iron/master
99084c6 Ignore vendor
f80d6ca Add composer
da54899 Add custom documentation script builder
68e5a49 Add PHPdoc tasks
a9510b5 add waffle.io badge
16bf682 Use up to date commands for coverage
aadcac6 Add code rating
4be70a3 Don't test 5.2
dced064 Update readme.md
496dfab excluded_dirs is deprecated
277134b Update scrutinizer config
6ff23df Add composer config and dev dependencies
93d76ec Make PHPUnit generate an XML for coveralls
b19656e Add scrutinizer config
de04025 Ignore vendor dir
b480376 Add a link to Help page
288b562 Move to activation hook
863fd4c Bump up required WP version
a42df0e Escape all the things
86dee22 Save errors to a notices option
275727b Reload page on errors
6cc016b Remove script
25fa141 Remove unneeded class
9fb9d09 Merge branch 'nice-errors' into issue-600
16f9a71 Check PHP version on plugins loaded
cb50705 Check PHP version on activate
ca0bdcb Merge branch 'master' into issue-599
ad7545a Merge pull request #522 from humanmade/issue-522
f3c1926 Merge branch 'master' into nice-errors
cd9f659 Update readme
7e56616 Set required version to 5.3.2
a1e232a Update tests
f5b647d Merge branch 'master' into issue-522
c3a4120 Merge pull request #567 from humanmade/issue-567
63828db Merge branch 'master' into issue-522
fc8dc0f Merge pull request #559 from humanmade/issue-559
ab910df Merge branch 'master' into issue-522
53dd5ec Merge branch 'master' into nice-errors
96463b5 Allow for a 30 second delta in asserting schedule time
28f3fee Merge pull request #603 from joshk/patch-1
b2e6b4d Use the new build env on Travis
7003ac1 Restrict plugin to be network only
ddc10dc Fix admin URL logic
80bac40 Merge pull request #571 from humanmade/codesniffs
7d372a7 Formatting
1554f59 Merge branch 'master' into codesniffs
a3360a5 Merge branch 'master' into nice-errors
3588d85 Update readme changelog
8ee1642 Bump version
aa02f24 Ignoe history log
f441eec Merge branch 'master' into nice-errors
a33db27 remove uneeded images
1bc5460 latest hm-backup
ed1cf87 latest hm-backup
a9d5bf3 Latest hm backup
ac9daea Added known errors and nice messages
d5ab157 Fix the support button splitting on 2 lines when too many tabs
74f7298 Spaces
4866fb7 Merge branch 'master' into nice-errors
19a7c14 Typos in v 3.0 changelog
8011d69 Specify POT filename in grunt task
feac2fa Update POT file
e86b19c Markdown readme
8452647 Regenerate readme
b6ed354 Add plugin headers
5f0ced8 Fix semicolon
7d94870 Merge branch 'master' of github.com:humanmade/backupwordpress
572479e Refactor the recursive filesize scanner
611fe90 correct text domain
028a406 Merge pull request #556 from humanmade/issue-556
d252312 Merge pull request #580 from humanmade/issue-580
f45eb75 Merge pull request #584 from humanmade/update-backdrop
6a5053b See if this fixes tests
b9bf7f6 Remove unneede statements
ab6d058 Use correct action hook
b4f9c9e Fix display notices
6ba1774 Set notices
cdf4b01 Formatting
c31db46 Merge branch 'master' into nice-errors
104c0ea reload the excludes filelist in the correct place when someone excludes a file
6a78aa9 Latest backdrop
1507855 Regenerate minified CSS
c6f6b19 Regenerate minified JS
f141d82 Fix cancel backup action
b18075d WordPress Coding Standards
1bf78f3 Exit early if incompatible version of WordPress
0371f2d Update translations
7d10add Update changelog
9135ff1 Merge pull request #573 from humanmade/design
834e55f Load minified CSS
026d280 Formatting
fd7f6f3 Biweekly wording
2baaa0f More Yoda conditions
9373e66 Spaces
61672e1 Comma after last array element
2fd458e Yoda conditions
f61f8cb Add missing period
27d076c use nonce_url instead of manually adding the nonce query param
309a57c close the settings form when done
f2cefe0 Design changes as per ticket
b965549 Start tracking langauge in server info
e2e1484 Right align the primary button in the enable support modal
b9302b2 Re-factor the directory filesize code to use a single array instead of thoussands of transients
fd5e4b7 Remove the warning that would show if you were using anything other than the latest stable, it's no longer needed now that the FAQ is local
2ec7406 switch to using a single transient to store directory filesize data
e7668ab Merge pull request #552 from humanmade/issue-552
ecf868b Merge pull request #562 from humanmade/enhancement/issue-562
66dfebe Add an anchor link
c10a760 Add error message
d9f2f64 Rename function
205355d Prefix GET params
4424535 Update exclude rule action
a40fb52 Adds function for building admin action urls
0bb6d12 fix vertical scroll
1349691 Adds some functions to manage settings form submission errors
cd5ca41 Rename nonce and action
bf5eeb4 fetch errors to display
1461319 Form submission handling for BWP and add-ons settings
2e753d6 Use a new function that persists form submission errors to  a transient
1379329 None check
8f8e84c Pass the nonce around in the ajax request
dd220c9 Enable support action links
db63646 Check nonces
689cf4e Modify action URLs to use the admin_post hook
b3926bf Remove unneeded code
be579ff New line at end
0b8a892 Use admin_post hook
784733f Merge pull request #502 from humanmade/stream-integration
e9d20dc Merge pull request #554 from humanmade/fix-display-schedule-time
6a3ac22 Display schedule start time in local timezone
4f20f32 (tag: 3.0.0-beta) Update change log
6342aad Remove duplicate file
f9ba00d update read me.md
010159a Update translatable strings POT file
8e93e09 Bump version
ca037bd Bump nom version
f6b3e6b Update min WP version and tested up to
73ba64d Bump version
f37c3dc Merge pull request #482 from humanmade/re-design
61f644d fix some more issues with time
7727c51 try fixing the time
d3c93b8 exclude tests dir from test backup
075023c PHP 5.2 compatible time mock
5fb1475 fix tests bootstrap
743f9b1 Update tests shell script
7aeb0f9 Update tests config
fcaa5e6 Use HTTPS URL
64d38aa Merge branch 'master' into re-design
7da213c Merge pull request #536 from humanmade/fix-transients
8eb71c9 Update tests shell script
ad16c2c Update tests config
d435898 Make it clear we want one week
f538a4b Display our notices - still WIP
b136062 Add a class to track common errors and their nice message
7331c01 Add a notices class.
5e6e858 Reload the page to display notices
480e56a Set our notices option in the database with the backup errors.
16d08a5 Handle the dismiss action for backup errors
afe325c Include the notices and errors classes
fa4a7a1 Add a singleton to handle known errors thrown by backups
29c5795 Add remaining disk space
e97f76b accidently used dash instead of underscore
4e76cf8 namespaced option and added option to uninstall.php
628486c basic show/hide of premium upsell
ee76b21 Merge branch 'fix-transients' into nice-errors
3e8060b Merge branch 're-design' into nice-errors
2eaa37e Merge branch 'master' into nice-errors
07e61d1 Set BWP WPR web hook url to live url
b870d0f BWP webhooks - 2nd iteration
1b4ce2a Fix incorrect transient expiry
13526d8 Add an action hook that gives access to consumers to the backup progress
0f82eb7 Merge pull request #406 from humanmade/issue-406
14bb5fc Show the spinner in the tab if a schedule other than the current is running
7ad8cdb Snip snip
5cf3737 Bring back the some javascript enhancements
bb41a2b Switch to the PHP 5.2 compatible version of Backdrop
f9bbe62 Finish up support
fb1a135 Brace up single line if's and foreach's
613100a Only load minified scripts and styles if WP_DEBUG isn't on
d656ee5 Load the minified css and js files by default
1fea51c Remove the combined css files as we only have one now. Stop loading colorbox.
0922885 Remove colorbox
259476d Merge branch 'master' into re-design
cc3bf2d Merge branch 'master' into re-design
332c84f Improvements
bb112ea More improvements
f33e735 Latest BackUpWordpress
43d1f7b Don't die when directly running a backup on page load
a03b0ab Re-factor the backup filesize calculation
4c1f49a make capability filterable
a8b4cbc use core capabilities instead of custom
0715c88 Switch to Backdrop
b250577 Merge pull request #486 from humanmade/feature/486-exclude-directories-default
94125e6 Fix typo in prefix
ee06cd5 Merge pull request #523 from humanmade/build-tasks
03c2ff7 Hook function onto admin_post
b3d776f Update delete link
72be8d2 Bookmark current admin page for redirect
44243ca Add custom capabilities and role
60815cd Exclude BackUpWP by default
0c97e6f Merge branch 'master' into feature/486-exclude-directories-default
e569fbb add fake endpoint
9cf9a82 Configure WP Remote webhook on instantiation
c170405 Inject the schedule to the constructor
33d8e59 JSON encode body
0d903b7 Sanitize URL
2952179 Encrypt the header with WPR key
a0e3ca3 Ignore the build folder
75e492d Add more build excludes
d3a8ceb minify JS
cd15331 generate markdown readme
0126061 minify css
737d1c2 combine css
17f8975 regenerate readme
1eeed38 Make links consistent for the grunt task
8a6d52f Convert URLS to markdown
f04f804 Update lang files
06eb230 Add colorbox as bower dependency
1d4066a remove colorbox folder
402129b Remove colorbox submodule
2015eb2 Change how we include FAQ
8b72677 Add readme partials
87e4cbf Add package.json
f70a6fd Add Gruntfile
f5253b6 Add bower.json
8d9760a JSHint rules
89975f7 remove from ignore
452320d Update ignore list
0e59aa8 Add bower config
f16e93a Add FAQ strings
344d9ba Return the cached directory size early if we have it
bac6613 Re-factor the file browser scanner
3fbcb3f correct sprintf usage
ba52842 Handle saving service forms
9aa9396 Merge branch 're-design' of github.com:humanmade/backupwordpress into re-design
c32babc Codeing standards
b882cd9 Move the error check outside of the foreach
38633d8 Remove uneeded $is_tab_visible
b515c6c Only show excludes for backups which include files
918c984 Show destinations in the list of schedule links
6e3a449 Merge pull request #514 from humanmade/issue-514
dc33eac Fix property name
12f791b Fix property name
aa90eaa Return errors
631b382 Add the remote post action
5b01a1e Start on the remote post
cd03423 Display and validate settings
0e3ab94 Include webhook class
cdf5085 Begin a webhook class
67e97b9 WordPress standard modal for enabling support
5e3e235 Remove extra slash in include path
778403a Add a heading to the settings form
069b7e0 More work on excludes
005fe7b Another todo
cd6c7b6 Add some todos
a36e27a Don't include the parent directory in a browsable list
c590af0 More work on Excludes
f0b1678 Merge branch 'master' into re-design
936bfde Switch to only storing 3 backups by default
29f7dfa More work on redesign
49f444f Merge pull request #507 from humanmade/update-travis-tests
31b7bcb update paths
0fef6aa fix plugin path for tests
7a06dab Change bootstrap
2bce541 Use the new develop WordPress repo for testing
aebfe53 Merge pull request #445 from elliott-stocks/enhancement-heartbeat
971bdfd Small typo in readme
4c039fc (tag: 2.6.2) Bump for 2.6.2 release
77255e3 Merge branch 're-design' of github.com:humanmade/backupwordpress into re-design
8372afa Merge pull request #495 from humanmade/revert-3e213ac
73200a8 commented out enable support button till we figure out what to do with it
a26419f made tabs responsive below 639px
7e3ff9b Revert https://github.com/humanmade/hm-backup/commit/3e213ac2bbd06d02383ed5290d6475cc1bed0c36
fc00c91 (tag: 2.6.1) Bump ready for 2.6.1
29ea240 Merge pull request #490 from rmccue/fix-tests
fa3b97c Merge pull request #493 from humanmade/bugfix/add-nonce-check
eb38af9 Add a nonce check to the schedule submit form
edcd9ff Add redirect to heartbeat tick
f8bb0dd More work on redesign
d7e1300 Remove unnecessary code, add heartbeat functionality
4feafb9 Remove hmbkpRedirectOnBackupComplete
c9ecd92 Enqueue heartbeat API
b2121e1 Allow output to be returned for AJAX requests
8eb475e Add heartbeat received filter
207791c Use long-hand ternary for PHP 5.2
d78df49 Remove namespaced code
d624d64 Add more default excludes
6d11b42 Merge pull request #481 from humanmade/bugfix/481-fix-schedule-hours-display-local
bef64d0 Merge pull request #487 from humanmade/bugfix/487-fix-excludes-rule-delete
f5f50b8 Revert "latest hm backup"
929a93c Remove resize_options var
6b516e5 Revert "latest hm backup"
b5ae8b1 Calculate local time for display
15a2e57 Correctly highlight the tab for the first schedule
2c3b3a7 Switch to tabs instead of subsubsub
44602bb latest hm backup
22768fe (tag: 2.6) Add a couple of missing change log points
a0c705e First bash at a redesign settings UX
ff4aa1e Merge branch 'master' of github.com:humanmade/backupwordpress
be23fbc Fix a minor style issue with long exclude rules in the exclude rules table
2478775 Hide tabs until the modal is fully open
f7e6c11 Merge pull request #477 from humanmade/fix-cancel
e20d3a2 Bump for 2.6
dab17ec Adds a missing id attribute to the max backup input so that the label works correctly.
8bc62e1 Fire actions for services first so that they come before the main status settings.
bbad481 Deletes the backup running file in the cancel backup action
349fb51 Some minor CSS / JS improvements for colorbox
8ad272f Merge pull request #476 from humanmade/issue/fix-prefix
04fc42d spacing
3487b08 spacing
1daf76e fix textdomain
5b0e1ad declare vars explicitely
c822fcb Merge pull request #428 from humanmade/running-schedule-start-time
2135da8 Merge branch 'master' of github.com:humanmade/backupwordpress
3d9f294 Avoid deleting the backup running file in hmbkp_cleanup
58a8118 Introduce get_schedule_running_timestamp and use it to show how long the current backup has been running for
43df7af Merge pull request #260 from humanmade/home-path-fix
78b5168 Merge branch 'refs/heads/master' into home-path-fix
669077d Merge pull request #459 from humanmade/button-spinner
ab829f1 Merge branch 'refs/heads/master' into button-spinner
1e944ee Pull in fix for home_path from upstream
1320452 Merge pull request #474 from humanmade/trim_multiple_email
7e2bee3 Merge pull request #372 from humanmade/feature/schedule-recurrence-settings
b10292a Move the spinner outside the button
124d3b4 Disable buttons while the ajax request they just triggered is running
2d07f4b Remove a redundant usage of sprint_f and correct the argument order for another.
e156229 Brace up and trim any whitespace from $email
9c6a602 Only call set_schedule_start_time if we have a start time
3ee4f6d Fix notice
fcbbce5 return 0 if we are passed a type we don't recognise
344d98c s/reoccurence/recurrence
5e61c67 Only show the total calculated schedule size when editing a schedule
86b1caf s/dpesnt\'t/doesn\'t
be40709 Don't strip 0 from minutes in the schedule sentence otherwise 10 becomes 1
39ab8ef Let's die instead of just echo'ing the error message as it's cleaner
fd3283c Introduce HMBKP::refresh_schedules to force schedules to be reloaded from the DB and use it when re-setting up the default schedules.
20b648d Finishes up the unit tests for hmbkp_determine_start_time
c123b35 Merge pull request #472 from humanmade/fix-cli
611cce0 Use updated syntax for WP CLI.
b8c230b Merge pull request #470 from humanmade/issue/470-update-upsell-link
27c37c8 Updates instances of bwp.hmn.md URL to https
f9e138e Re-factor the underlying logic that allows the schedule time to be set + unit test
971f444 Merge branch 'master' into feature/schedule-recurrence-settings
6f0cacc Merge pull request #463 from humanmade/remove-deprecated-function-463
9116508 Remove deprecated function and fix translatable string
2972dee Merge pull request #461 from humanmade/various-typos-fix-461
c75e504 Corrected 'back ups' typos
70e7f05 Cleanup whitespace
c72c269 Hours and minutes can be 0 so we can't use ! empty
071cba7 Revert to previous state
ec64df7 Merge branch 'master' into feature/schedule-recurrence-settings
53e886c Merge pull request #455 from humanmade/constant-help
261b370 Minor improvements to the server info tab
f756417 Merge branch 'refs/heads/master' into constant-help
9fd2841 Merge branch 'refs/heads/master' into origin/feature/schedule-recurrence-settings
8db93e6 Minor copy / layout improvements
091b3ec Float the time fields right so they match the style of the other fields
9dbe724 Merge pull request #456 from humanmade/unreadable-root
e268787 chmod the custom path so it's always possible to remove it
251123b Make sure the directory we are about to pass to RecursiveDirectoryIterator is readable
235ff2b Avoid a notice if there aren't any schedules
d653463 Zebra stripe the table
21cc2dd Don't allow the plugin to function if the root dir is unreadable.
ee0c87f Improve the layout of the Constants help panel
46dbc0e (tag: 2.5) Bump time
6f1949b Remove the old plugin.php file, having it symlinked didn't work anyway
60f9e7c Stop passing $_SERVER to Intercom
3657fc2 Show long strings on their own line in the enable support popup
1d3587c Improved positioning for the .subsubsub spinner
2a637d7 Merge branch 'master' into feature/schedule-recurrence-settings
21cbb74 Merge pull request #426 from humanmade/pass-display-name
712fa56 Merge pull request #420 from humanmade/pass-bwp-version-intercom-420
a2b2473 Merge branch 'master' into feature/schedule-recurrence-settings
ef0e2e7 Pass display name instead of nickname
7b0bd20 Merge branch 'master' into pass-display-name
42f67b5 Merge branch 'master' into pass-bwp-version-intercom-420
97f1a36 Couple of line breaks missing
af74250 Merge pull request #371 from humanmade/wp-is-writable-function-371
c36350d Merge pull request #427 from humanmade/pass-timeout-intercom
efc592e Merge branch 'master' into wp-is-writable-function-371
77c5c76 Update UTM
f4fb3f0 Clean up readme
94193bb pass display name to intercom
68832dc Send max execution time to intercom
338033a Add Plugin version to server info
403920b Merge pull request #446 from humanmade/close-php-session-446
6286e2f Merge pull request #443 from humanmade/use-new-spinner-443
326c3bd Merge pull request #450 from humanmade/contributing-instructions
4fb0f98 Translations instructions
d653fb4 Merge branch 'master' into feature/schedule-recurrence-settings
04d1814 Merge pull request #442 from humanmade/minimum-3-7
c44a934 Use new spinner
7a6bb3e Fixes an issue on servers which only allow a single session per client
cfa942c Made sure resize_options is defined inside catchResponseAndOfferToEmail
37749d1 Merge pull request #434 from humanmade/filterable-from-email
24c9a9e Merge pull request #441 from humanmade/update-lang-files-2.4.2
8728da9 Make the from email address filterable
a94d8d0 Bump the readme to require WordPress 3.7.1
1d5de52 Stop testing against 3.6
7311226 Get rid of some stray double line-breaks
31cc2e3 Stop checking the minimum supported PHP version
d632660 Remove back-compat time constants
a3839d2 Bump the minimum requirements to WordPress 3.7.1
45c624a Merge branch 'master' of github.com:humanmade/backupwordpress
71c2f54 master is now 2.5 alpha
f9d5748 fix email address
152625a Update text strings for 2.4.2
1edb037 latest hm backup
7d4de70 Merge branch 'master' into feature/schedule-recurrence-settings
659a124 Merge pull request #407 from humanmade/safer-redirects
fd826b0 Remove stray line break
2d6b0e2 (tag: 2.4.2) Readme for 2.4.2
a064ca7 2.4.2
0726166 2.4.1
03baa8a Merge pull request #324 from humanmade/multisite-admin-324
58eece6 merge master into current branch and fix merge conflict
9edbf3d Merge pull request #394 from humanmade/load-bwp-first
77d346d Merge pull request #440 from humanmade/travis-test-wp-3.8.1
4217648 Merge pull request #437 from humanmade/filesize-failure-437
dc1339d Merge pull request #439 from humanmade/intercom-file-sizes-439
f3d07ce suppress error messages for filesize
84897fc Get calculated sizes of active schedules instead of calculating on every page load
74b23dd Merge pull request #417 from aubreypwd/master
cf29bc0 do not test older versions of WP
68b670d test with WP 3.8.1
5147559 Merge pull request #438 from humanmade/shell-exec-test-432
95b586f test for function availability
07569fc Merge pull request #433 from humanmade/fix-php-notice-433
a4310d5 Merge pull request #432 from humanmade/shell-exec-test-432
5344978 test for availability of command
9613f80 Fix PHP notice in default excludes functionality
7e11ff5 (tag: 2.4.1) Bump stable tag
e0b5390 Bump for release
6546fd3 Merge pull request #412 from humanmade/exclude-cache-folders-412
1b49d2e Fix resize_options
139da4e Modal fix for long paths
f3cb4e7 Fix issue where modals showing underneath WP Admin bar
7ac0c0a Add trailing slash to found folders
8e0c55d Add trailing slash to excluded folders
5a0b4c4 Code formatting
7365f17 Exclude cache folder by default
5bccad8 ensure bwp is activated before addons
439917f fix merge conflicts
1cb3651 Test against PHP 5.5 and WordPress 3.6/3.7/3.8
604c004 Merge pull request #411 from humanmade/rename-filesize-transient
d6f5994 Rename file size transient to contain the backup type, so we don’t need to clear the cache when a schedule type is modified
fe66aa0 Merge pull request #405 from humanmade/use-correct-escaping-functions
09ef19f Merge branch 'master' into use-correct-escaping-functions
a410fc9 Merge branch 'master' into safer-redirects
f135020 colorbox changes
923fa00 latest version of hm backup
49d3d6f reset hm-backup submodule to previous commit
44efeea use wp_safe_redirect
cd7d7b3 no need to internationalise non language attributes
67316bc formatting and spacing
becb46b Latest HM Backup
0037829 Merge pull request #402 from humanmade/revert-cherry-pick-time-settings
22c3efd remove the time settings that were wrongly added
2ff6ed9 Merge branch 'master' into feature/schedule-recurrence-settings
1e76c20 resolve merge conflict from cherry pick
20d41e1 Reload page on close modal so settings are refreshed
c84d40a Branch out logic by detecting if submission was from destination form. If so, no need to process recurrence settings. Just service settings.
4bbf4df Reload page on close modal so settings are refreshed
5a19f66 Test recurrence settings
315bf8d adjust CSS
efa03c6 use a div
d983941 escape square brackets in ID selectors
ba79dd0 wrap min hours with label to keep together
5a910ba move service validation
5a51719 use 24 format for input, remove AM/PM setting
ee9cb46 only show twice daily note for that recurrence
a54f489 make weekday strings translatable
f24bd73 change textdomain
cd52ef9 delete old backups before saving settings
b1376b2 docblock and else curly braces
05fd873 indentation and formatting actions.php
6ba5ad3 prefix javascript functions
2fa06a9 Merge branch 'master' into multisite-admin-324
0a7bca1 Merge pull request #393 from humanmade/travis-encrypt
5456f14 New encrypted hipchat API token
eb3b8a2 Merge pull request #387 from humanmade/fix-transient-387
4f0155e Latest HM Backup
ef4a4b5 use get_transient to retrieve value
118753e Merge branch 'master' into wp-is-writable-function-371
6461824 Merge pull request #391 from humanmade/feature/service-intercom-data-function-390
5e3019e add the service constants to the intercom data
21d7849 display any service constant
842557e just return an empty array for now
f714c4d alternate function for display
e52e13d intercom_data should be static so we can call it with call_user_func
b5e196a add the ATTACHMENT_MAX_FILESIZE email requirement constant
e9a6f60 email intercom data is managed by BWP requirements class already
e63a263 Merge pull request #389 from humanmade/bugfix/swapped-arguments-path-accessible
862db2e Merge pull request #390 from humanmade/feature/service-intercom-data-function-390
8f79d47 adds abstract function intercom_data
0d95733 input validation improvements for schedule form
31fe7bd return false if not set
5e262f2 arguments were swapped in the function that checks if home path is contained in the backups dir path
3615f44 set default schedule type
85bd820 only instantiate schedule if no errors
dfaa12f we need this without instantiating a schedule
53bbf89 set recurrence when setting start time
edada0e better validation
488aaf0 make sure there are no errors before saving
838f858 Merge branch 'master' into feature/schedule-recurrence-settings
8e8c20c add default day of month
19b8043 change input default value
0aba13c update schedule tests
4ae2feb use set schedule start time for default schedules
835670e default arguments for setting schedule start
3e38b6a fix backup action URLS
1708a6e return zero instead of WP_Error
f2b314c schedule form field validation
70d091f more network_admin_url
ecd1995 stupid mistake
0c344b2 fix syntax error
0954b51 use network_admin_url
bb98cbb update more references to tools.php
0d6d33c Merge pull request #377 from humanmade/server-info-help-tab-377
67878a3 refactor by using a constant and only 1 conditional
d5f15ef Merge pull request #381 from humanmade/use-wp-mkdir-p-381
fa5ade1 Merge pull request #303 from humanmade/invalid-reoccurence-fix-303
061c7dd we should not use the constant here as it may not be defined.
335934f sets schedule start time for manual backups
16fde51 check that var is set before output
3d27331 schedule start time is now an option
e298fc0 if the recurrence type is invalid just force it to manually
8df5d08 adds server info tab to help screen
c442a8d replace mkdir with wp_mkdir_p
bdaf86c move BackUpWordPress admin to network settings on multisite
4ede7ac Bump required version to 3.6.0
3ee284d Use wp_is_writable wherever is_writable was used.
2da238d Update CONTRIBUTING.md
f985cfb Update CONTRIBUTING.md
5126579 Update CONTRIBUTING.md
3247144 Update CONTRIBUTING.md
cdd9787 refactored the schedule recurrence logic
d89a74b Add new schedule UI and logic
525a856 do not define the schedule start time constan by default
f2eb346 Merge branch 'feature/schedule-recurrence-settings' of github.com:humanmade/backupwordpress into feature/schedule-recurrence-settings
0f31c11 prefix attribute
b0f80f9 more recurrence logic
33d87c3 hide / reveal recurring settings based on chosen schedule
d43f03f adds the day and time fields to the schedule settings form
53711e2 Merge pull request #379 from humanmade/update-po-mo-files
8eaba4e Merge pull request #380 from humanmade/update-colorbox
8efc03f update to latest colorbox
3d49129 Merge branch 'master' of github.com:humanmade/backupwordpress
cd1ecab add new updated language files
3a29a70 updates po/mo files with latest strings
e2544a5 Merge pull request #376 from humanmade/dont-hide-delete-links
a72bea6 Release notes
3ce9d7a Correct translation function
7409e35 Latest HM Backup
1201ee5 Bump and release notes
2146eb3 Only hide download links when the backups directory isn't web accessible as deleting will work.
ddd5d67 Merge pull request #366 from humanmade/enable-intercom-support-366
b85ef87 Code comments
e48d1ab Make a string translatable
7138bb2 Organise tests into more logical groups
1492f3f Store the result of the wp-cron test so we can pass it to Intercom
dc9f415 Stop sanitising test names before passing them to Intercom
cd8d6af Add new tests for site_url and home_url
9882fbd Better name for the support schedule that is created to calculate the backup size
8e208c8 Plugin filename should be backupwordpress.php not plugin.php
ab54dfd prefix attribute
6f3f689 Use the new option name in deactivation and uninstallation
91957c3 Merge branch 'enable-intercom-support-366' of github.com:humanmade/backupwordpress into enable-intercom-support-366
0c91659 Move the support opt-in flow to be part of the support button and generally improve things.
67255b9 Code comments / formatting
1e869c2 more recurrence logic
a6214c0 hide / reveal recurring settings based on chosen schedule
49cf5c6 Merge branch 'master' into feature/schedule-recurrence-settings
50ea2be delete optin option on deactivate / delete
91e71ed prefix functions
0d9565f Merge branch 'refs/heads/master' into enable-intercom-support-366
f7aaeec Fix a notice if $services isn't defined.
66299ff Merge branch 'master' of github.com:humanmade/backupwordpress
0f23353 Bump
7a5bb3b Merge pull request #375 from humanmade/no-backups-colspan
d20677f Ensure the message shown in the backups table when no backups have been completed spans all 4 columns
d500312 Merge pull request #286 from humanmade/disable-dl-link-286
c31ebd6 Merge pull request #288 from humanmade/pass-page-slug-as-var-288
aa793c1 Merge branch 'master' into enable-intercom-support-366
ff0ef9e adds a button and a colourbox modal with server info
ca91ca2 refactoring
1fba846 add requirements class from compatibility branch and the server table output
2825763 reload page on settings change
a5fdbfd adds the day and time fields to the schedule settings form
b71ee59 Merge pull request #370 from humanmade/correct-language
58eb3c5 remove some unnecessary code
3185ff5 spacing
a446d50 adds an option checkbox for intercom
9f3e115 spacing
b5699e3 add intercom user hash
653ba19 spacing
af22b2d check if path is accessible before displaying download link
60299b7 correct some language
a38818a pass page slug as var to js
b5e7ef4 schedule sentence escaping
c71eaa9 Merge pull request #369 from humanmade/upsell-pro-addons-369
d51c007 rename add-on to extension
911aba0 Merge pull request #368 from humanmade/fixes-uninstall-file-refs
0963fd3 adds an upsell message to the footer of the main plugin page
123feb3 enables intercom contact and tracking
75176a6 fix wrong file paths in uninstall
4874655 Merge pull request #361 from humanmade/password-field-width
b00011d Merge branch 'master' into password-field-width
3fae243 Merge pull request #364 from humanmade/better-schedule-sentence
9dfe5b5 Improve the way destinations are handled in the schedule sentence in 2 ways
a3e8e2c Merge pull request #362 from humanmade/schedule-title-status
c06a7fe Merge pull request #363 from humanmade/esc-schudule-status
8cc3746 Use wp_post_data instead of esc_html and status's can contain html.
ffaaf21 Show the running schedule status in the title attribute when hovering a running schedule title (that you are not currently viewing)
f5ba48b Slightly re-position checkboxes
504f137 Force password fields to be the same width as text fields in the model forms
91c888c Merge pull request #346 from humanmade/dev
6cd0e6f Merge pull request #354 from humanmade/dont-escape-plain-text
0c53304 no need to escape the email address
7e7e8b3 Merge pull request #352 from humanmade/formatting
4c57e93 Merge pull request #353 from humanmade/prefixing
b333c74 Merge pull request #355 from humanmade/escaping-email-address
e8d6b6d Merge pull request #358 from humanmade/get-slug-condition
81333b1 Merge pull request #359 from humanmade/remove-openbasedir-heck
b4622f2 no need for this check, already handled elsewhere
4359c85 slug could be set to an empty string, so check this
9bf881c use echo esc_attr on non tranlatable strings
e925dd7 is_email already trims
2619f72 few escaping fixes
f3ae151 prefix functions
7a1a913 remove extra line returns
04de7d3 limit style to text input
a8bf160 resolve merge conflict
8b53c84 Merge branch 'fix-excludes' into dev
0cc97c8 exclude WP DB Manager default folder the correct way
5178f63 use stable version of hm-backup
06a9af5 really add the escaping
196fc78 more escaping
814cac5 escape on output
c4e4a12 WP Standards formatting
db82139 bump version
304aad7 Merge pull request #345 from humanmade/change-filenames
7361bab Merge branch 'dev' into change-filenames
68ab430 Merge pull request #343 from humanmade/enqueue-fix
73d8465 fix merge conflict
a699cc0 Merge pull request #344 from humanmade/title-translation-337
1372013 change version back
6daa045 french PO-MO files ready to translate
9a1d35c introduce a backups_number function
43afad9 few internationalisation fixes
40839ac keep string in one sentence
2958288 make schedule titles translatable
c7da92b Merge branch 'master' into enqueue-fix
31abee9 enqueue differently to fix colorbox failing to load
f2dadf3 Merge pull request #339 from humanmade/fixes-open_basedir-warning
0263fa2 don't use $schedules var if its not set
3e68fa8 nioce error message
345eb5d constructors dont return
8ac306b Merge pull request #336 from humanmade/dev
6d6941a v2.3.3
44be3bf fix enqueud style src path
fdf3253 (tag: v2.3.4-alpha) v2.3.4-alpha
e759433 Merge pull request #333 from humanmade/dest-form-logic
332cf3b Merge pull request #307 from humanmade/fixes-307
6c1282c Merge pull request #334 from humanmade/exclude-leftover-bwp-folders
e40f395 formatting
021ea52 adds a function to exclude leftover backup folders
3787e47 check if path has changed
36d3994 Merge pull request #332 from humanmade/fixes-332
b8bd2f0 removes extra slashes in enqueue source path
c602a22 form close button logic
ff86c78 refactored include path
9d62136 use WP standard file naming
4b446e8 Merge pull request #327 from humanmade/exclude-backupbuddy
fdb5077 refactored default excludes function
e8fd153 excludes backupbuddy default folder
6ebc8da Merge pull request #326 from humanmade/sched-sentence-325
0968d27 Merge pull request #292 from humanmade/use-wp-error-292
d697ecf only show addon sentence part when service is active
5336d74 Remove old test/lib submodule
826ee0e 2.3.2
a6b8a1e fixes unmatched closing parenthesis and docblock
85b439b replace last Exception
d1bfb62 replace more exceptions
650284b Merge branch 'master' into use-wp-error-292
89de7a3 Merge pull request #323 from humanmade/adds-latvian
e5f5dcf add latvian lang files
871ca07 Update CONTRIBUTING.md
d688862 Merge pull request #322 from humanmade/contributing-file
fab67ce instructions
b316d37 Merge pull request #321 from humanmade/fix-remaining-sched-instantiation
b3eccce fixes left over direct instantiations of singleton class HMBKP_Schedules
4f0697a fix conflicts
e28653d Bump
a66ab31 Updated Readme
e27fed3 Revert "Merge pull request #304 from humanmade/update-close-buttons"
f60064a adds wp db backup to excludes
a0b1693 Merge pull request #320 from humanmade/changelog-2.4
a758156 2.3.1 instead of 2.4
d807d75 cleaning ip
859e729 adds default excludes and removes ability to delete rule
7cb471f Ignore the .svn repo
27c6281 Merge branch 'master' into backup-folder-excludes
b0946fd update change log for 2.4
5d91d3f Merge pull request #304 from humanmade/update-close-buttons
5269e6f check if services array is not empty
e0fcf3d Merge branch 'master' of github.com:humanmade/backupwordpress
fc9d1f2 add default excludes array and setup on schedule init
aa874ea Merge pull request #282 from humanmade/singleton-schedules
feb900e Merge branch 'master' of github.com:humanmade/backupwordpress
09e7669 add default excludes array and setup on schedule init
f113843 make HMBKP_Schedules class a singleton as it contains all the schedules and only need one instance
71a3ee5 PHP Docblock
1cb9a9c replace Exception with WP_Error error handling in 2 places.
a8dcff8 Merge pull request #315 from humanmade/fixes-undefined-notice
271807e declares  and initializes it
42def6d Merge pull request #301 from humanmade/fixes-broken-local
bd42c22 Merge pull request #294 from humanmade/updates-lang-files
4118772 Merge pull request #296 from humanmade/better-schedule-sentence
ca95e99 Remove "These external locations" from schedule sentence
d5ec251 Merge pull request #299 from humanmade/contrib-guidelines
b5dd322 Merge pull request #305 from humanmade/fixes-297
1018be8 Store the return value of wp_mail in $sent so we don't send multiple notification emails
3cbeeba Merge branch 'master' of github.com:humanmade/backupwordpress
f0f668e fixes #297 typo in option name
c250471 avoid undefined error
1dcb1e2 save and close are separate actions
939de53 remove commented out line
a810ae9 fixes #300
52acd9c Disable email notifications for Travis builds
467bb37 create file
06cb2ac Merge branch 'better-schedule-sentence' of github.com:humanmade/backupwordpress
1304540 Merge branch 'master' of github.com:humanmade/backupwordpress
7889da2 Whitespace ftw
359cc21 Merge pull request #295 from humanmade/new-unit-tests
f2c0661 implode on comma
1eb874d make schedue sentence more consice
42a242b Update the Travis
4184643 Switch back to using WP_TESTS_DIR instead of hardcoding the path
ed09bfa Rely on the WP_TEST_DIR environment variable instead of shipping the whole wp-tests dir with the plugin
1b0c3e8 s/add_command/addCommand
551bc26 Remove extra linebreaks
74dca7c Bump
f0095a9 Fix a PHP strict error
b8a695a updates lang files
e478f98 Update the path to lowercase now that we've renamed the github repo to be lowercase.
a2c4ace Setup our wp-tests-config.php file
1697012 Tag as released.
452c93f Move dash inside of string
9da8cfc Remove the trailing slash from the backup path before checking it's validity
a78358b Merge branch 'master' of github.com:humanmade/BackUpWordPress
423c901 Bump ready for release
e8f1d8b Merge pull request #229 from humanmade/single-calculating-thread
8773324 Laetst HM Backup
155156e Revert the changes to assertArchiveContains and assertArchiveNotContains in favour of introducing new methods
31d1f53 Normalise slashes in paths
b75830f Normalise paths before comparing them in assertArchiveEquals and assertArchiveNotEquals
6167a7b Bump
c463181 Always delete the backups directory after each unit test
6461e10 Coding standards
502d34f Prefix the backup path with backupwordpress so it's obvious where to look to find your backups
a20440b Remove stray error_logs
63e785d Bump
5ce9138 Re-calculate the backup path on upgrade and move any existing backups there.
46d7b95 Don't access the hmbkp_default_path option directly as it may not be set.
2df5eae Correctly calculate the HMBKP_SECURE_KEY
f8e2a19 No need to wrap hmbkp_init in a function not exists check.
0ba4ba7 Remove stray line break
38aa2ed Don't indent the copyright notice
1acb085 Bump for pre-release
d4e5b4e Remove the help text for the HMBKP_EMAIL constant as it has been deprecated.
7aa1b16 Latest HM Backup
d6929cc Don't allow the filesize of the site to be calculated in multiple thread at once.
0596cdc Don't highlight the HMBKP_TIME_CONSTANT example if it's set to the default setting as the constant is defined in the plugin
faaa524 Correct hipchat room
7eba138 Remove square brackets as they break travis.
c73e61b notify hipchat of build status's
68b3d2e Merge pull request #284 from humanmade/fetch-destination-settings
3ea959d adds function to copy settings from previous schedule
6d050fc Code comments
222849e Don't allow a scheduled backup to run if it's already running in another thread. Will prevent issues where load balancers and proxies re-send requests that don't return within some arbitrary timeout period
613ccc9 Beginnings of a HMBKP_Error class
3857efc Code standards
7462055 Latest HM Backup
e65220d Whitespace
65160ec Make the exclude help string translatable.
8841bd9 Set a maximum height when displaying the error message so it doesn't cause the modal to be larger than the page.
f33a1d8 when moving the backups directory, don't delete the old one if it's outside of WP_CONTENT_DIR
bcd01a3 Only move zip files in hmbkp_move()
821dd9d If HMBKP_PATH doesn't exist then use hmbkp_default_path()
b05975d Don't delete non-backup files in custom paths
28e4512 Code formatting
5400d39 Ensure the database dump is uniquely named per schedule to avoid possible collisions when multiple schedules are running at the same time.
bca2783 Backwards compatibility for the time constants which were introduced in WP 3.5
48e365a Don't bother testing all version of multisite, just test master
c70df6f Stop testing in PHP 5.5 until it settles down
4ca88b3 Remove PHP 5.3 ternary operator syntax as it breaks when running unit tests on PHP 5.2
89a5749 Test against all major releases of WordPress since 3.2.1 across all major releases of PHP since 5.2
293c4f4 Latest HM Backup with all unit tests passing locally
123c880 Reference the plugin using a case sensitive path in the phpunit config
e996f9c Switch to a https checkout for the lib submodule
d47259d Switch to our fork of the test lib
00ef12b Latest test lib
34992e2 Latest HM Backup
8dd4e9b Only test against a single instance of WP for now
6d57cc3 Tell travis to recursively clone in all submodules
581e2c2 Add the travis configuration file
c075f16 Switch the submodule clone url for gm-backup to https
c19960e Merge branch 'master' of github.com:humanmade/BackUpWordPress
1872998 Make the unit tests phpunit compatible
42c679b Add pauldewouters as contributor
bf306f3 Don't try to update the manual reoccurrence during the 2.2.5 upgrade routine.
2e9ecd0 Add a line break
344e850 Code formatting
5355300 Use correct escaping functions
487383d Re-jig the maximum backups help text to make it more concise.
97f2392 Remove trailing tab
4b5844d Whitespace
f8d5864 Remove duplicate is_string check
e15c62f Whitespace
d571fcc Set the initial width and height of the colorbox and set the transition to elastic.
a6f8d1c Upgrade any stored schedule reoccurrences to use the new naming convention.
64e034f Code formatting
1971bdb Untab the whole file
6a9b384 Use single quotes and add missing space between closing quote and parenthesis
37b3284 Merge pull request #257 from humanmade/dev
2c3dcda Merge branch 'master' into dev
73e3e97 Merge pull request #273 from humanmade/varname
cd3f1b1 underscores instead of camelcase for consistency
793a970 refreshed mopo files
b4dc5ae add new function to load translation files in a flexible manner, add POT file for translators, regenerate PO and MO files
8eae498 add a new function get_cron_schedules for filtering cron schedules
1222714 fixes Docblocks
7e3f476 remove random debug plugin version
ae1450f Merge branch 'master' of github.com:humanmade/BackUpWordPress into dev
7c392fc Merge pull request #263 from thomasclausen/patch-2
3e154bd Merge pull request #264 from thomasclausen/patch-3
4f29425 update docblocks
1b85f50 do not remove option prefix
6a9aaae deleted a log file
8dd078b changed main plugin file name for consistency
6f92376 custom cron intervals need to be defined as their own array with the interval as key
ce81c5a update interval names in more places to avoid fatal errors
8bc348b updated schedul interval name with prefix in several locations
4dc7f1e schedule enhancements
941cc58 added missing schedules param and merge custom schedules
b7437b1 use constants in schedul intervals
7ad2db1 just some indentation
bed981f remove duplicate activate function causing fatal error
289d0e1 fix docblock
f891fe3 add activation function and internationalize message
3c1d7ad corrected typo in message text
7d5f3fa fixes #262
2af8543 Merge branch 'master' of github.com:humanmade/BackUpWordPress into dev
5a59a64 indentation
92436fb Merge pull request #267 from thomasclausen/patch-5
7fb077f Missing translation
0c63da9 Merge branch 'master' into dev
8242be8 fixed bug in colorbox error message display
202366a input[type="number"] is too small
f04e78e Missing translation
fc6dbe4 move the max backup size after description
20da959 change wording of max backup size
f21e1d1 remove unnecessary vars
99bc4ab new function get_formatted_filesize
a3d7e56 fixes #255
806e031 Use correct filename for Danish translation files
9270246 Latest HM Backup
2e3a353 Slight refactor, remove need for variable variables
53eb85b Correct @return docblock param
e96d8c5 s/de-register/unregister
98fb94e Code formatting
75bbd3b Set abstract methods to public as they are expected to be implemented in child classes as public
b49f557 Set the @var to the class that the variable will contain an object of
c7c24ba Correct @return in docblock
c13e2b0 Remove an unused variable
892bc12 Don't store the return value of wp_mail in an unused variable
2412774 Make sure we always return a string, even if the conditions are not met
cf6825c Correct docblock
5452dd2 Fix a docblock
34ce62f Introduce abstract protected function is_service_active() and use it in the email service
3d2da20 Improved styling for popups which contain tabs
fa0872a Improved error message styling
dc6023b Merge pull request #249 from humanmade/colorbox
1376383 Fix some styling on the new colorbox popups and ensure it resizes properly throughout the excludes process.
6f4ee67 fixed a bug where jQuery alias not available
8fc2ff7 colorbox lightbox width
e553bc0 Merge branch 'master' of github.com:humanmade/BackUpWordPress
aae12c2 Latest HM Backup
c729622 dont hardcode slug
6c161ae deleted fancybox
d09062e Use correct constant for HMBKP_ATTACHMENT_MAX_FILESIZE
ea88d36 resize after adding buttons
943096d removed remaining fancybo references and submodule
d8ad331 excludes form width
6916f65 replaced fancybox with colorbox
5b0d868 Merge pull request #247 from humanmade/dev
243b4e1 resolved conflicts
f34622f fix bug in service settings
72bd165 added property to toggle service tab visibility
a2a4671 resolved conflict
dc29250 Merge branch 'master' of https://github.com/humanmade/BackUpWordPress
7ee581d Bump for release
1fb986b Use call_user_func to call HMBKP_Service::constant for each service instead of the php 5.3 only way $service::constant()
00566e8 Bump for release
39d4a8c Code reformatting
f1ae908 Fix a parse error
4b23e80 (tag: 2.2.2) Updated release notes.
9e0f523 Update translations
1463878 Minor text improvements
a8af5ae Update original strings
d2cf0f3 Bump and release notes
abdbb84 Silence possible warnings when unlinking
0871bb2 Minor code formatting
5684313 moved the destinations menu link
f46d61e add property to toggle tab visibility
798bf11 Merge branch 'master' of github.com:humanmade/BackUpWordPress
61ca652 Latest HM Backup
97ab36a Merge pull request #245 from pdewouters/master
596123e Latest HM BackUp
ca4bd02 removed quotes wrapping a nonce var
82e563c Merge branch 'nonces'
ec68546 removed unnecessary lines and did some formatting
12b186f replace all calls to exit with die for consistency
5ca6b17 added nonce check to all ajax post actions
0210692 Merge pull request #243 from pdewouters/master
77028d0 cancelled the slug capitalization
ffbbdbf added human readable name for services
77bda92 reverted 2 commits
e32ce59 Merge branch 'master' of https://github.com/humanmade/BackUpWordPress
52ac62f add name property
7de9e1d Doh, fix a stupid fatal error
e059087 Pass back an empty array instead of all service options when asking for a service option that doesn't exist.
f92a8bc Make constant() a public method.
43d296c make actions menu extendable with apply_filters
c1e0b69 Latest HM Backup
503b3ae You can't have protected abstract methods since PHP 5.2.
27be1d8 use plugins_url for assets, fixes case sensitive 404 error
15293a7 fix plugin URL constant capitalization
5a42c04 Latest HM Backup
838831e Add a docblock to the abstract constant method
6bd1f44 Update readme
fed0192 Ability to set the maximum email attachment filesize
9a17eef Fix possible notice and Fatal error when uninstalling
111a7af Only try to add the FAQ if we were able to connect to the plugins API.
fc9fe8c Released 2.2.1
754fa00 Changelog for 2.2.1
6c5b162 Force 500 error header for testing (commented out)
6bfba16 Strip tags from error messages
91bef0f Catch server errors during the ajax backup process and display them to the user
7a236d2 Fix JS error and use correct class
804c458 Only output an error / warning message if there are errors or warnings
126bcb1 Changelog for 2.2.1
3eb573b Bump
79597cf Latest HM Backup
c0bad9e Display errors and warnings in error popup after backup
eecfe58 Catch all types of fatal error in backup process
8645f7f Preserve whitespace in the error pre tag
a950698 Don't redirect if we have an error
b85cd76 Write errors and warnings as they happen.
71af0ea Fix PHP Strict warnings
4803568 Mark static functions as static
4969597 Released
1dcbc5e Chinese translation
a1a7d37 Serbian translation
aa703f7 Russian translation
9fe56db Romanian translation
566d8e9 Portuguese (Brazil) translation
d1ea675 Polish translation
e15e487 Dutch translation
5fb564f Latvian translation
f2d5afb Lithuanian translation
bcf6f0b Italian translation
280620d Hebrew translation
0728c2f French translation
3711134 Basque translation
3b739a2 Spanish translation
3c3f02e German translation
b754430 Danish translation
531f9fc Czech translation
064cf16 Latest po & mo files
9c710de Bump for release
1dbc5db Bump - close to release
0860b48 Revert "Don't define private internal vars"
56daef6 Latest HM Backup
2c9a9d4 Cleanup on uninstall
a55c892 Formatting
418640e Don't let hmbkp_rmdirtree delete directories outside the site root
7e3bcfd Cleanup the deactivate hook, no point removing non-existent options
27d2510 Explain yourself
fe8e817 Handle situations where HMBKP_SCHEDULE_TIME isn't defined
4a7309c Switch to using activation and deactivation hook functions rather than calling the actions directly
ce5dab9 Add a test for fortnightly
56464f6 Add unit tests for each of the schedule occurences
7e2f57a Make sure we cleanup after ourselves
bb356ea Add our custom cron schedules to the default cron_schedules array so that we can schedule events using them
b92af3f Fix possible notice
18ec091 Move .po and .mo files to languages folder
f9ca49b Latest HM Backup
fe2a42c Don't define private internal vars
7b49f4e Don't esc_attr unless we are outputting
45f9179 Fix possible warning
efddfa2 Only update backup type if it's changed
3d47ce1 Namespace our script localizations
32ba1de sanitise and escape all the things.
df48893 Increase the timeout on the ajax cron check to avoid errors on slow sites.
6f6ed69 Sanitize some shit.
26ddd39 Stop defining PCLZIP_TEMPORARY_DIR outside of hm_backup as it shouldn't always be set to hmbkp_path()
ae3212e Some code cleanup
4930b4c Latest HM Backup
df27971 Use realpath to check that the path resolves somewhere before checking isReadable
2409ef0 removed duplication of media query rules
64d50ce Merge pull request #219 from humanmade/Mediaquery
ab00e92 media queries for modal buttons
bacafc5 manage excludes modal styles fixed. added retina spinner
83ef61b delete old backups before the backups list is displayed and also before a new backup is run to catch instances where the backup process fatal errors after creating the backup file but before delete_old_backups is run
0c04f05 revert deleting old backups in hmbkp_cleanup.
1e9ba82 Remove old backups as part of hmbkp_cleanup
74113fc Run hmbkp_cleanup on load of the admin page to help keep things clean
5cd35c9 Replace the last 2 instances of wp_get_schedule missed in the previous commit
d3b95af Code formatting and clenaup
5020b49 Define our own list of schedules rather than relying on wp_get_schedules as that can be filtered by other plugins which can cause unexpected consequences.
b933aab Merge branch 'master' of github.com:humanmade/BackUpWordPress
b8cb3ac Also include the legacy SECRET_KEY when checking for user defined auth keys
37787b4 Bump time
ac0287d Include any user defined auth keys and salts when generating the HMBKP_SECRET_KEY
c4e49e6 Use the existing HMBKP_SECURE_KEY to calculate the randomised prefix for the backup path.
b84f426 Merge pull request #211 from humanmade/fix-for-service
cc9b732 When data is being saved for a service, default to empty array, as using input type=checked will cause it not to be set
812f48e Make set_status() public, so services can update the status of a backup progress
41d8437 Create readme.md
fa36380 Start on changelog
74bf0f8 Bump
e5b8493 Use dirname( hmbkp_path ) instead of WP_CONTENT_DIR to account for custom backup paths and when the path is set to uploads.
6dfc256 Correct logic so we only generate and save the default path once.
00f364c Bump for release
ef8719d POST not GET, fixes previewing and adding exclude rules
ec5a323 Bump for release
538eb12 Latest HM Backup
953984d Exit don't return on error for ajax requests
f5fcc35 Treat '0' as empty when checking ajax responses as some servers return 0 even with exit('');
6a6c268 Spelling correction
9b66689 merge with master
033781f Bump
4382251 Fix a PHP notice on Apache servers
6f991a0 Bump
ec42544 Latest HM Backup
289b0c2 Correct dot file ('.' & '..') check
9c22d5b Filter out blank statuses.
2bc4fc4 Check global $is_apache instead of calling mod_rewrite_loaded as that function seems to cause issues on some servers.
5483864 Remove errant error_log
7e1e201 Bump
82ac4bb Latest hm-backup
e78dbd2 Don't call url_shorten as it's only available in the admin, just str_replace instead. Fixes fatal errors when WP Remote triggers backups.
9452dcb Don't load the whole of misc.php for apache_mod_loaded, just call the function directly.
728c8b9 Move the function_exists, file_exists and is_writable checks into the parent if as there is no point running any of the code just to fail at the second if.
c7d5c45 Merge branch 'master' of github.com:humanmade/BackUpWordPress
0fdfd07 Merge pull request #191 from humanmade/fix-misc-include
8b5b30c fixed including misc.php
02d46bf Don't hardcode the english string for Update, instead use the translation.
d7ff153 fixed including misc.php
f4e96e2 latest hm backup
a5e1876 Release notes for 2.1
2dd8dbf Bump ready for release
ee6a0f4 Latest translations
0d3e027 New originals
ad10f6f Merge branch 'master' of github.com:humanmade/BackUpWordPress
a010894 Move placeholder to help text
3e25ec8 Define the var outside the if
c11ff1d Improve the performance of the exclude files modal by iterating directly through the DirectoryIterator instead of storing the whole filesystem in an array.
fdd9d92 Latest HM Backup
628aeea Don't stop people with safe_mode = On from using the plugin, instead just show a warning message.
ae94736 Add a next backup time tooltip to the hourly backup sentence
976c89f Update the link to the restore backup post on hmn.md
121148f Point people to the FAQ before telling them about the support email address
5511b82 Add a line about rating the plugin on the plugin directory.
4313d71 Bring back .htaccess protection for the backups directory on Apache servers
c235714 Create the backups dir in the uploads dir if it can't be created in WP_CONTENT_DIR.
d036fff Remove the "remove" link whilst the exclude rule is being removed.
b2a326a Add the spinner back to remove exclude rule
01120c3 Mark the backup as running sooner
37c8d96 Better check for default exclude
5c188e9 Don't esc_attr vars that aren't being echo'd
4193396 Get don't post
13d888e Minor text improvements to code comment
3937e5a Don't redirect the original backup request in case it hasn't had chance to start yet.
ef29112 Increase the time between polling the server for status updates to give requests a chance to finish
d962d7a be more specific as we use hmbkp-running in more places
813bc6a A way to force memory errors
8f67ba9 Improved status messages
84b15c7 Show the spinner next to the schedule link when a schedule is running and you are viewing a different schedule.
730bc54 Bump
0c3450c get not pot
b5746aa Add correct class to cancel button
41c84b7 s/_/-
70082c6 Bump up the ajax interval
07ea6b7 Always set the redirect arg
4e39f11 dash not underscore
0aac32d Bump
bb79b1f Bump
c05b34e Make sure args are passed through recursive calls to hmbkpRedirectOnBackupComplete
1d1f415 Bump
7ab99fc Catch Fatal errors that occur during the backup process and offer to email them to support@hmn.md
20eca40 Display "Starting backup" if the status hasn't yet been set.
5075764 Latest HM Backup
dbcad72 The running status should override the error status
fed73a2 Remove the error class when a new backup is started
613a188 Latest HM Backup
9d4e471 Bump
48db33a Latest HM BackUp
4cf0cc8 Include archive and mysqldump method and verification steps in the status messages.
ab105b6 Catch Fatal errors that happen during the do back ajax request and display them in a popup
1bad676 Catch and Display E_ERROR errors on the do backup ajax request
1a75167 Check for constant changes before we call hmbkp_path
276c086 Release notes
efb3658 Latest HM Backup
141922e Remove HMBKP_ARCHIVE_FILENAME
422551d Prepend a random string to the beginning of the backups path
05a47a4 Improvements and unit tests for moving backup path
01dddf8 use sanitized url instead of site name in backup filename
0372abc Latest HM Backup
8d0dc69 Better cleanup after unit tests
45b945f Make sure we have a plugin version saved before comparing against it. Stops update actions firing on first activation.
184c917 Bump
096326b Allow the archive filename to be overridden.
f4f9a49 Remove use of realpath as it causes issues on shared hosts which use symlinks for users server root.
308b9b9 Don't attempt to download a backup which doesn't exist.
9419082 Don't urldecode the urlencoded base64 string.
85087e3 Don't throw an exception when the schedule start time isn't an int as they don't have to be.
646dddc Updated original strings
1744b94 Bump
241faf7 Fix possible warning on update if cron is empty
b7cb90d Don't show the version warning for the constants tab as those are pulled from the current version not the repo
3400e1e 2.0.5
d65efb2 use a proper version comparison when checking whether this is an update from 1.x to 2.x
2eaa879 Specify 'i' directly as a time format instead of relying on the user set time_format when calculating whether a time is an absolute hour.
55fd182 Convert to user set schedule time to UTC before comparing against now and if it is in the past add interval instead of "tomorrow"
c4a393e Docblocks
0bdc9ca Introduce a new constant HMBKP_SCHEDULE_TIME to allow the schedule time to be controlled.
0f76aff wp-cron should check for a non 200 response
1619fa1 Whitespace
5d01df2 Re-schedule on __construct if the schedule has become unscheduled somehow.
4c29912 Use the WordPress built in size_format instead of defining our own function for human readable filesizes
ce0ca9b Remove all hmbkp schedules on deactivate
b442a80 Remove line break at end of file
b6591ab use wp_retrieve_response_code instead of accessing the response array directly and attempt to show the response description alongside the response code.
c6b3f4d Use wp_remote_head instead of wp_remote_get to speed up the wp-cron.php response check.
21b9307 Bump
927043f Revert change to the way the plugin path and url are calculated as it broke some installs
cfe0637 Fix some unit tests
83e5cac 2.0.3
5af28c0 Merge branch 'master' of github.com:humanmade/BackUpWordPress
dc85d6e Fix PHP errors when you try to activate BackUpWordPress with WP Remote already active
6b5cfd6 Only call array_flip is the $errors array is populated, as it can be NULL which will cause a notice
72d869c Bump tested up to version
f96b2ed Remove TODO and whitespace
ed2d5de Allow HMBKP_PLUGIN_URL to be filtered
3a0ae30 Bump the minimum version check to match version in readme
5c95f91 Remove unused constant
efaf8b4 Latest HM Backup
ed9af8a Don't use strict operator to check 200 response
5098825 Fixed scheduled backups (by using a common hook for all), added get_schedule() function to HMBK_Schedules, split setup default schedules to it's own hook so it can be removed,
856ca7f If the cron request is_wp_error() show different message
9fe931a use dynamic paths, as this means you can have the plugin in a theme / embedded in another plugin
90ed393 Added PHPDocblock
ab1fbd1 Remove empty bullet
356eb6f 2.0.2
da7faf5 Remove the memory limit error message for now as it's causing more trouble than it's worth.
db5fb5f Merge branch 'master' of github.com:humanmade/BackUpWordPress
92a5109 bump
4a39b52 Catch wp-cron wp_errors
f00ab65 Make sure we have a running backup filename before doing a file_exists and an unlink, fixes a possible warning when backup_running_filename is false and thus we try to unlink hmbkp_path
52da406 Only send backup failed message if the backup file doesn't exist.
a1adc00 2.0.1 fix fatal error on PHP 5.2
40dd2f1 Getting ready for GM
5fffb7d Move the screenshot outside of the plugin
e905875 RC 1
642dee9 Add a couple of missing esc_attr's
f131b5f Protect against a possible Notice if there are no excludes.
91cc071 Protect against a possible notice
7eb4cca Don't remove the scheduled_id param when redirected so we don't lose our place.
7abaf15 Reduce the time between status ajax polls. Fire the initial status check straight away.
f13bc07 Scrap that idea.
56b7694 Don't pass .php to get_template_part
1988899 Attempt to hide that the backups dir even exists by showing the 404 page.
44dee09 Remove all query args before redirecting back
850d9ad Nonce, escape and i18n
b2c9b00 Fix PHP Warning
a027720 Add a missing legacy option for removal
325af18 setup the default schedules after update has been fired so we don't get default schedules as well as the legacy updated schedule
22c791c Don't check the return value of set_type as it doesn't return
f0713fa Set the parent excludes in set_excludes
13dfb05 Class shouldn't be escaping
963aeaa No need to set_type of parent class on construct
acd1898 set correct type
a71cfe4 Set the legacy schedules start time if HMBKP_DAILY_SCHEDULE_TIME is defined
7279090 Properly upgrade manually only settings when creating the legacy schedule
54bbf5a Use correct sprint_f arg
11e4446 Use the ajax url
4bd341c Don't load a file that doesn't exist
6d01616 Latest HM Backup
f423ebb Only set excludes if they are different
4d3a666 re-org some functions and delete and unneeded file.
6a63d93 style the default and defined excluded file reason
3138673 Use proper english
9e29427 mark default and defined excludes
c15e3f3 Skip the test if a custom backup directory is in use
8bf37ac Bump
4bae0e4 Don't allow the backups dir or defined excludes to be removed.
be0f3ea a's now use the ajax url directly.
db7f864 fix adding new exclude rules.
390f603 Allow backup path to be overridden with a define.
28399e1 Typo
bba3f72 Don't double escape the backup filename
2995cb7 Use the Ajax urls directly as there is no non-js fallback for now.
7c16e60 Lots of work making BackUpWordPress work better in low memory environments.
cdfa519 Redirect to the new schedule on add schedule
ca57a7d Latest HM Backup
c3a2cd0 Fix wp-cli command
e33fd1d include the spinner gif with the plugin as we can't reliably guess the location to wp-admin in CSS
a290c3c Latest HM Backup
712e4fa Properly highlight the selected file list tab in excludes popup
3a06e1b Add some missing docblocks
a5f3c46 Clear the cached filesize when excludes or backup type changes
2e53742 Correctly store the calculated filesize in a transient.
5fa64db Bump
13e3e75 Escape DB_NAME
5441035 Unit tests and improvements for manual only backups
57e97cd Merge branch 'master' of github.com:humanmade/BackUpWordPress
0bba9c4 s/Feedbask/Feedback props @herb_miller
c967acf Merge pull request #146 from elektronikLexikon/master
7970180 %s %s to %1 %2
667e7df Ability to have manual only backups
b059ba0 Latest HM Backup fixes #133
c575bcf Latest HM Backup
859d73c Fix for when unit tests are run in a WordPress in a submodule env.
72574d9 Use default black overlay
4675fe9 todo
720e210 Make it possible for PclZip to be targeted specifically.
aa4105f Delete the running backup file if there is one when a back up process is cancelled.
90b7e20 We don't use modernizer
43c1d72 Update translations.
f42d31d Merge pull request #144 from elektronikLexikon/master
1d36444 updated German translation
8cda712 Bump
71b686e Branding
1119601 allow argument swapping in email translations and move the email out of the translatable string.
e687b29 Move compat check to the top so we don't waste cycles on older versions of WordPress.
85cf577 Latest HM Backup
81c607c use HM_Backup::get_home_path in place of ABSPATH.
27b099b Correct readme.txt
bd0bdc2 Merge branch 'refs/heads/master' into 2.0
fe024cb (tag: 1.6.9) 1.6.9 changelog
c45194d Support downloading backups when your site is in a symlinked path.
c4f5a14 Merge branch 'refs/heads/master' into change-content-dir
cd50cfe 1.6.9 bump
5b3dd92 Merge branch 'master' of git://github.com/elektronikLexikon/BackUpWordPress
6866e09 Strip ABSPATH not root from exclude rules.
42c40a0 Calling a static method through a variable Class was not supported until 5.3
d5ea971 s/humanmade.co.uk/hmn.md
caa8ab3 Fix check for timestamp
1e37953 Use root not ABSPATH
003435f Inverse logic
d54f821 Remove debug cruft
cc99d14 Unit test schedule and changes to class to make it more testable.
208ee1e Don't remove non-existent backups
e264bcc Latest HM Backup
01241cc Latest hm-core
e4f65d6 Fixes to Schedules
fb2220e Some additional js strings
fd1711d Fix fatal error in unit tests
161b278 Delete extra backups if max backups is changed to below the number of existing backups
ed0b6d8 Remove old settings on upgrade and clean up whitespace
1eb8846 Fire update action for downgrades as well as upgrades.
9b6b1c8 Convert legacy schedule names on update.
67e1989 Migrate legacy settings into the legacy schedule on update to 2.0
0024569 Remove some old messages
942e63b Don't mention day in schedule sentence for daily schedule.
4cc93df Correct comment
748fd57 Proper entity for less than
6c030a8 Fire update actions in chronological order
d131f4d setup a legacy schedule when updating from V1 to V2.
c63ce1e Improve default schedules message
c863044 Switch to using plugins_url with the first param as it handles symlinks.
b029f1a Access static methods directly instead of using a wrapper function.
f9ab14f Access static methods directly instead of using a wrapper function.
9d80ca9 Improved comment.
5ae7ac6 Make consistent with the PHP error message
e18f9d2 Use __FILE__ instead of manually building the path
b6206a0 use plugin version when enquiring scripts and styles.
619a606 use plugin_dir_path and plugin_dir_url instead of manually building them.
d55a688 Use hmbkp_get_home_path() instead of ABSPATH
d348533 Actually… there is a function that does this.
51012bd Don't use ABSPATH here - because that is the worpdress directory, rather that site root.
a9005ab (tag: 1.6.8) 1.6.8 readme
d174b40 Updated spanish translation props @radinamatic
86fddbc 1.6.8
e068f27 Bump
be7a7b0 Documentation for the new HMBKP_ROOT constant
602ed0a Merge branch 'refs/heads/master' into 2.0
cdd94a7 Updated Russian translation.
756111b Romanian translation
fd69c42 Serbian translation props stefan
cfc7942 Lithuanian translation props vincentas
c7aceda French translation props christophe
d3dfa9b Updated Spanish translation props Radina
f8ceee1 Default schedules
772bd90 Derive backup type from backup filename so we don't incorrectly label old backups when a schedule type is changed
9900396 Email notifications
ad768b8 Better replacement of ajaxurl as it's sometimes relative
226b938 Avoid error if no schedules are setup, we'll have some proper schedule setup at some point
7a5fbf9 re-org + more work on stuff
32a32d9 Show label and improve styling of add new exclude rule field
69dd917 Remove unneeded class
6ca965e edit excludes separately to settings as it creates a cleaner user experience
15db12b Updated translation files
5680910 Allow constants to be translated.
8ab9541 Updated translation files
3796dff Merge branch 'refs/heads/master' into 2.0
35a8217 Updated pot file.
e4c0c17 Move .htaccess into sprintf arg
2ea85b5 Move link into sprintf arg
5ca3405 Add a link to translate.hmn.md
fb67fc7 Make contextual help tab titles translatable and add more missing text domains
284cad3 Don't translate whole a tag
7a41fa6 Add missing text domain
1c814eb Make "Settings Save" translatable
bdefe85 Make "Save Changes" translatable
5162bd6 rejig sentence structure so they are more translatable.
f3b26bd Make Cancel translatable
35709e9 Delete schedule, delete backup, localise js strings, more php string translation.
b843f89 More work on schedule UI and logic
c1df8d1 			throw new Exception( 'That backup wasn\'t created by this schedule' );
834ab32 We're not using this
ec33561 Latest HM Backup
062c88d Remove .DS_Store
0e7f4c2 More UI work
aa2397e Unit tests work, schedule class done, started work on new UI
8dab4e1 HM Backup 2.0 beta
b61833d Add fancybox
3b32b29 Allow root to be overridden.
5a1db5d Don't store invalid email address's
600770a Don't load HM_Backup if it's already defined.
79e7201 chmod 644
3ddc906 (tag: 1.6.7) 1.6.7
9870513 HM Backup 1.5.2
f12c956 Cache plugin data in a transient for a day to avoid a remote get on every page load.
048be08 whitespace
648a42d Support entering multiple comma separated emails.
f040c6f s/to/too
65206aa line break
3c4cd99 Merge branch 'master' of github.com:humanmade/BackUpWordPress
14bd967 krsort instead of ksort so that backups are returned in chronological order.
73edf6b Use correct property when setting the mysqldump path
1c79e47 Merge pull request #103 from radinamatic/patch-1
e533057 Hi Tom,
b99c123 Bump
d7e7b06 HM Backup 1.5.1
41bf3b7 release notes
21132ef HM Backup 1.5
e5e6ddc Bump
e5b9bec Make secure key override-able
d05983b Latest HM Backup
39736fc check get_email_address() instead of HMBKP_EMAIL
a481bd7 Clear email error on cleannup
e008d54 Code formatting
de5645a Send email at end of backup process so fatal errors don't stop backup from completing.
619d260 Code formatting
2602e42 whitespace
f629358 @todo
1410adb Make sure backup file is attached to email.
d21bd19 Make sure file_exists before deleting.
37eb48d Store running backup filename in .runing_backup then use it to make sure we don't show partial backups in backups list.
f3374b0 Use better filename checks in hmbkp_cleanup
30cb215 Fire error on failed backup
b2833c7 Proper capitalization
ae00fcd Bump
f7397ac Don't cache ajax requests
87fecec (tag: 1.6.4) 1.6.4 readme
c3021d3 Pull upstream
3719063 Delete .htaccess on update so it's always rewritten and check <IfModule mod_rewrite.c> to avoid 500 error on servers without mod_rewrite
5c77f6e Pull upstream
1a49838 PHPdoc
eacb15e Don't show message for warnings as they freak people out to much and cause people to think the backup has failed when it hasn't
6fa9cc0 Pull upstream
6b6115d Code formatting
a04b5fb Pull upstream
bd661e5 Use correct operator
1316011 (tag: 1.6.3) 1.6.3
e9744b2 No need to add backup path to excludes as it's auto excluded.
f679a72 hook email backup into hmbkp_complete_action so that fatal errors in sending email can't break backup.
8551aa3 Define PCLZIP_TEMPORARY_DIR earlier to ensure it's always set to backup path.
755b787 Pull upstream
864ae59 Pull upstream
d433c96 Introduce HMBKP_SECURE_KEY and use instead of SECURE_AUTH_KEY
cfeaaf5 Better error message text
5c74fc2 Don't strpos blank ABSPATH
62b4103 (tag: 1.6.2) 1.6.2 changelog.
d2b8280 1.6.2
2db2e2c Code formatting.
3479438 Load admin_actions earlier so they can hook into admin_init
e3982dd Ability to dismiss the backup error / warning messages
c90d541 Pull upstream
74f49eb Clean up some obsolete update code.
8578a6d Don't clear hmbkp_max_backups option on update.
c6be2c9 Don't send backup email if backup failed.
24c91a9 Avoid NOTICE when no errors.
c42bab6 Pull upstream
a540d17 Only show warning message for php errors in backupwordpress files.
7f8fcda Mark the button as backup started and settimeout to 500
73b7a5b (tag: 1.6.1) 1.6.1 release.
b257307 (tag: 1.6) Bump to 1.6
fc99e52 Return button even if the status is empty.
defd817 More obvious that running backups can be canceled
cb82321 Use getter methods instead of accessing properties directly.
693da83 Pull upstream
cae995a No need to set root as it defaults to ABSPATH
193e138 Don't echo time() in full backup test.
def211d Pull upstream
40bc667 Incorrect comments
67c1cc4 Pull from upstream
d832205 Show a message for backup warnings.
7edfa8c Cleanup on errors
e2802b8 Cleanup on errors.
94bc92f Pull from upstream
bd914ec Make cancel backup work with new ajax backup
6ce5e27 Remove Constant as it's no longer needed
7d4b536 Fire manual backups using ajax, completely removes the reliance on wp-cron for manual backups.
28f7fa9 Fix notice if backups dir isn't readable.
8296a80 Nicely formatted errors in backup error message.
f265d19 Store backup errors in a .backup_errors file and show a message in the admin if there were errors in the last backup.
cea6d48 Pull upstream
1a06b37 Test archive_method, mysqldump_method and errors in unit test.
47068b7 Backup directory is now automatically excluded.
aeff432 Pull upstream
c152520 Minor code formatting
11f0099 Pull upstream
5afdb0f Pull upstream
ffbfc66 Allow direct http downloads.
96ef2d2 Remove actions when running backups from unit tests.
3f261b6 Use files() method instead of duplicating code.
eb69aff Pull upstream
6f6be0e Latest hm-backup
8ffbc00 Measure time in full backup unit test.
2c816bc Consistent handling of symlinks
826cdb1 Pull upstream
c7a84f8 Skip full backup tests until symlinks are properly handled.
e1e3e9a Unit test for a full backup
fcab193 Merge branch 'master' of github.com:humanmade/BackUpWordPress
4f13942 Pull upstream
8071a9c silence rmdir and unlink errors
05b58ba conform ABSPATH to normalise trailingslash on windows
1708eea Add Email info to FAQ and start changelog for 1.5.2
61bbdd3 Bump
baaef5e Minor code improvements, skip unreadable files in backup size calculation, use RecursiveDirectoryIterator in rmdir_tree
85180bd Skip unreadable child directories in RecursiveDirectoryIterator
5624aa8 Better help and fix possible error in backup path checks
02a5593 Support passing excludes through wp-cli
95998b7 (tag: 1.5.1) 1.5.1 changelog
32b56d8 WP CLI support.
10013f4 Minor code formatting.
633d2c0 Release time.
789a58c Pull from upstream
a8e48b2 Don't delete user settings on de-activate.
04162ad Bump
1273217 Use a DirectoryIterator instead of a recursive open_dir for hmbkp_calculate.
da9b8cf Only exclude backup path if it's in web root
ea2acf8 Add the warning to the top of all the tabs.
70dbe74 preventDefault to stop the anchor being added to url and to stop page jump.
e29ff76 (tag: 1.5) 1.5 readme
3160894 Ability to override the capability used to register the menu page.
a69d82c Suppress filemtime errors
99a79b2 fiddle with the order and remove ABSPATH before preg_matching to better match the plc_zip logic
641ec22 Pass defines straight to correct properties for command path.
1cbb2cc Latest HM Backup.
14247ef Always delete transient on save settings.
c1b3109 Back compat JS on old versions of WordPress.
c63d4ee Latest HM Backups
a4a157a Latest HM Backup
8b68c4e Pre 3.3 compat for help tabs.
ba7f621 back compat for 3.1 when WP_MAX_MEMORY_LIMIT wasn't defined.
f73d114 Latest HM_Backup and more renames
c382e42 Latest HM Backup
1a8025e Bump + code cleanup.
a8525f3 Add plugin FAQ and constants to help and convert to use new 3.3 help tabs.
49c0f7c Call conform_dir statically.
2998149 Rename Advanced Options to settings.
66fad96 Get backups working
b2f0202 Latest hm-backup
7286524 Load the HM Backup Tests.
9d71836 First bash at using hm-backup
516e5f5 Merge pull request #15 from valericus/patch-1
b0a8f3e Set proper charset of MySQL backup
8b1c3c7 (tag: 1.4.1) 1.4.1
4ed46d2 (tag: 1.4) 1.4 has gone golden.
f91a1d4 Fix a couple of last minute bugs.
2b9d335 New screenshot for 1.4
3b294c0 Finalising 1.4
bb531a0 Merge branch 'master' of github.com:humanmade/BackUpWordPress
97e9479 Code formatting.
b21cb67 Rewrite incorrect comment.
594e7ca Missing line break in .haccess comment.
e24cc2d Code formatting.
7e9f2ad @todo
f9b5a4a Updated Readme
630f55e Merge branch 'master' of github.com:humanmade/BackUpWordPress
43f17b9 Should use the function for checking this - for backwards compatibility.
57568ae Do not setup backup schedule if the option has been set to disable backups.
08e7651 Rename the backup schedule function.
aeb8cd7 Clear the schedule if the automatic backup is disabled.
056ca13 Add class = code to the excludes text area.
3bdbc3b Code formatting.
fb46f82 Minor PHP comment error.
93019af Correct author and plugin urls.
952b4f7 Correct github url
e4e8425 Add Theo to contributors list and order alphabetically
3aa9342 Bump
10cdd57 Merge branch 'refs/heads/admin_gui'
82d55f5 Code commentino, formattino & I18N
07068cf Updated language.
240e4ca Merge branch 'refs/heads/master' into admin_gui
26da9e8 Remove cruft.
f7f1576 Localise dates.
a2d3273 Merge branch 'master' of github.com:humanmade/BackUpWordPress
2691a21 Use correct translation domain.
e93883c Russian translation, props Valera R
e52bd8e strtolower instead of checking both lowercase and capitalised
9687d19 Merge branch 'master' into admin_gui
61bfb20 Bug in i18n - thanks Valera R
97e1447 Bug in i18n - thanks Valera R
4385235 Looks like our cron schedules filter got lost in a merge back there.
7fc9f1a Merge branch 'master' into admin_gui
7c8b151 prevent notices when the plugin cannot connect to the WordPress plugin repository.
eee9059 Fix typo in constant.
0637a16 BUG FIX - typo in the constant
f8507a2 Switch to use hmbkp_get_excludes()
ee15d43 Rewrite function for getting the list of excluded files/directories
b95b9a0 replace hmbkp_daily with standard WordPress daily
ee180fc Use the default daily schedule rather than registering our own
358dba8 Merge branch 'master' into admin_gui
97964cb Add an explanatory comment to the .htaccess.
7eb2b14 Constant to disable the use of wp-cron with manual backups.
40f6099 bump
627d400 (tag: 1.3.2) Version 1.3.2
bb5af87 Ignore unreadable files in PCLZIP
30928ec Properly export binary data.
a28656e Spanish translation.
6c4d1b1 Bump min PHP version to 5.2.4 to match WordPress.
b412439 Use 303 redirect when redirecting form submissions.
4655a80 If the database file doesn't exist after doing a mysqldump then fallback to the PHP fallback library.
f84fb70 Move set_time_limit outside of loop.
cfd6da5 Don't store .gitignore
a983c42 3.3 Style buttons
d32cf03 Stray line.
477d848 Better comments
1a1ebfd remove the last couple of bits of theos code that snuck in there.
6eafe41 Revert "Added DB entries for backup archives"
c984020 missed some stuff
9a254e3 Merge branch 'master' into admin_gui
b5970c2 improve the descriptions.
f825524 Revert "Added DB entries for backup archives"
5de95f0 call deactivate on update to clear bad settings.
59348db Merge branch 'db-logs'
3c592a8 ignore
40302fc Handle empty passwords in mysql_dump
9f9b80a Added DB entries for backup archives
0da2efb - Call deactivate on activation to clear everything out. A better cleaner solution. Thanks Tom.
d01c0a3 Merge branch 'master' into admin_gui
00f5d5c Fix
f1fd0c2 - Instead of deleteing the transient, we should delete the .backup_running file. Should maybe do this on activate as well just in case something had gone wrong.
00b0033 - Display advanced options panel if hash is set. - Close some tags.
c7e2bed - FIX - only show invalid no of backups if the field was actually submitted (note - disabled fields are not submitted)
e6decbe Merge branch 'master' into admin_gui
a58e4b2 - Update readme & stable tag
a132ab7 FIX add check for PHP Version, and die if less than 5.0
f0b4d16 Merge branch 'master' into admin_gui
bb5b787 - hmbkp_get_backups should return false if no backups.
2be96cf - Advanced settings form should be visible if there are no backups.
5b5eb6c - get_backups() should return false if there are no backups.
4865793 - Display a notice to say that all files in the root directory of the site will be backed up if there is are no excludes set. - Make the function for advancing the schedule by the interval simpler.
52d2d38 - tidy up
0ef77d9 - Some functions seemed to get lost when merging! - Fix some notices.
5a78ad7 - Fix some issues / duplications etc when caused by merge.
9b99f73 Merge branch 'master' into admin_gui
7cce37a Docs.
bfefb57 We no longer need mysql_ping
aa4608b Store running status as a hidden file instead of in the database.
975a4f9 - Remove an old function
48403f1 - Update readme
ca43c93 Don't show remaining space or warn when space is low as it's too unreliable.
30f8dc0 (tag: 1.3) Version 1.3 Gold
83acf1e Pull the FAQ into the contextual help section on the backupwordpress page.
efb8d10 Don't activate on old versions of WordPress
531bcac Overhaul excludes to support excluding absolute folders /wp-contet/, folder fragments .svn/ and files *.php.
e219bf7 - Improve scheduling of the new cron jobs. Make sure it resets at the right time, and only the right time. - Better commenting
8ce735d - When setting a new schedule - the first event should be advanced by the schedule interval.
df6d34c - FIX - make sure the schedule is cleared when it should be.
a2ab152 - Use deactivate_plugins() rather than manually unsetting. Thanks Joe.
8c8e097 Merge branch 'master' into admin_gui
3dce375 - Deactivate Plugin & Die if WordPress is too old.
09b101b - Update readme a little.
4cfff8a - FIX display real next scheduled.
7db7b35 - Maybe they shouldn't be capitalized after all. - remove bug testing code.
ae49c2b - Clear schedule hook when changing schedule setting. - FIX: capitalize display name inline with wordpress default cron schedules - FIX: naming of option.
93c87ca - FIX: make sure all options are deleted when the plugin is deactivated
1fc1002 - oops. missed some commas.
35238bb - add weekly, fortnightly and monthly to cron schedules.
e751d74 - Add setting of backup frequency in the advanced options form. - Save frequency settings.
2374007 - Fix the scheduling so that it works in all timezones, correctly. And certainly doesn't schedule the event in the past so that it runs backups constantly.
0996bf3 Don't attempt to guess compression, just display uncompressed size.
8cff239 Wrap ini_get( 'safe_mode' ); so we handle both (bool) false and (string) Off.
c7a7f32 - Save file with correct localtime - Show correct localtime in table.
5e11b63 - Adjust scheduled event for local time. - Display correct localtime.
b6ad6a1 - Stop even trying to guess the compressed size as it is totally inaccurate. Be honest, and just tell them the uncrompressed size.
bb15ff7 - Use php version_compare function to check versions.
050a7b5 - FIX - used the wrong key.
7a9a2ae - Move Advanced Options form notifications to the interface.functions file - and hook them in to admin_notices
34880f1 - FIX: Just some isset checks on my $_POST data. Thanks Tom.
0ef1c6e - If new exclude rules - delete cached est backup size stored as transient so that it is regenerated
f7b1e0f - Do not count excluded files & directories when calculating estimated filesize.
315bd03 - Fix - When submitting the form - you did not go to the top of the page.
b6cad30 - Better handling of errors when processing the advanced options form. - Display some nice helpful messages.
d6e1436 - Fix some of the text in contextual help
7985cc4 - Add 'settings saved' notification - tidy up
4e5e609 - update & add check to see if readme used is from the actual version in use and if not, display some warnings.
c74e6ee - Add FAQ to  Contextual Help dropdown - FAQ is taken from readme on wordpress repo.
92e04c4 Merge branch 'master' into admin_gui
479e1d2 Set database stored_filename directory rather than relying on str_replace.
763b8f8 Better hmbkp_path default
99bd09b Handle singular and plural for completed backup count
d2b5033 Better styling for advanced options.
de48557 Merge branch 'master' into admin_gui
dccdc32 - Do not hide the advanced options form if it has just been submitted.
a46533d - Fix message at the top not displaying the right message when the options form has just been submitted.
1fd7a3d - fix message not displaying correct option - hmbkp_disable_automatic_backup
c3c1374 - get excludes to use stored option
1b39875 - move save options function to admin.actions and process on admin_init - add some checks/nonce fields etc.
65abfed - change everything to use my new option value functions
be9c254 - more switching to use of individual functions to get value of settings.
09ee9d1 - move checking of max_backups to max_backups function
453f54f - Do not delete stored email address just because new one is invalid. Just return error instead.
bd25c5c - Advanced options GUI - Options page save function - beginning of a Wrapper function for returning either defined setting, or stored option.
197c346 Replace * with non greedy regex wildcard for PCLZIP.
ed85a9e Don't match against invalid exclude rules
5cd78dd Trim whitespace from exclude rules, fixes issue with comma [space] separated list of rules.
9dd836b Show examples for all advanced options.
3764099 Add support for excluding directories via a define.
dc78e1e Replace \\ with / in windows paths not the other way round.
65f0322 Support dynamic excludes in both zip and PCLZIP, lays foundation for user excludes.
f1b5173 Use consistent function names for admin_notices.
7beaad1 Properly handle setting and changing backup directory.
3223b24 Improve the get_backups code.
3c1411b Tweak FAQ
53c0d59 Merge branch 'master' of github.com:humanmade/BackUpWordPress
0789452 1.3 bleeding
5241d51 Correct handle for Matt
3d20f86 Merge branch 'master' of github.com:humanmade/BackUpWordPress
48102f5 - Update FAQ in Readme
b6e1607 (tag: 1.2) Version 1.2
da8e478 Tweak langauge.
03e35da Tweak messages.
887db23 Don't show message if email is invalid
673450b Merge branch 'master' into backupwordpress_email
1300f42 - oops. left in some debug code.
98b2b49 file mode change,
410b121 - Add some error messages for invalid email addresses and emails that failed to send.
f74e0a4 - Add ability to email a copy of the backup to a defined address.
8879ebf Merge code from settings.functions.php into core.functions.php and delete redundant file.
2b5a6db Don't hardcode Windows drive letters.
3851dce Merge branch 'master' of github.com:willmot/BackUpWordPress
87eabb9 - Icons - 32x32, 16x16, 16x16+hover - Add css for icon to hmbkp.css - Change screen_icon() to use backupwordpress icon - Icon for git repo
02e8a7e chmod moved files so we can delete them.
f4bd99c Check for wp_error in wp-cron.php check
40f0a36 Initial Import
948b600 Committed to much
b126a23 Initial commit

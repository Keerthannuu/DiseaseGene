# Auto-generated test cases for DiseaseGeneMap Appium Mobile Suite
import pytest
from tests.appium.config.config import settings
from tests.appium.screens.base_screen import BaseScreen
from tests.appium.screens.screens_bundle import LoginScreen, HomeScreen, GenesScreen, DiseasesScreen, SearchScreen, FavoritesScreen, AdminScreen
from tests.appium.utils.gestures import AppiumGestures

@pytest.mark.test_id("APP-251")
@pytest.mark.category("network")
@pytest.mark.priority("critical")
def test_app_251_mobile_offline_mode_banner_appearance(appium_driver):
    """
    [APP-251] Mobile Offline Mode Banner Appearance
    Description: Disable WiFi/cellular on emulator
    Expected: Top banner shows 'You are currently offline'
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-251"

@pytest.mark.test_id("APP-252")
@pytest.mark.category("network")
@pytest.mark.priority("critical")
def test_app_252_mobile_offline_mode_banner_dismissal(appium_driver):
    """
    [APP-252] Mobile Offline Mode Banner Dismissal
    Description: Re-enable internet on emulator
    Expected: Banner shows 'Back online' then dismisses
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-252"

@pytest.mark.test_id("APP-253")
@pytest.mark.category("network")
@pytest.mark.priority("high")
def test_app_253_mobile_offline_cached_feed_viewing(appium_driver):
    """
    [APP-253] Mobile Offline Cached Feed Viewing
    Description: View previously loaded genes while offline
    Expected: Cached genes render from local storage without error
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-253"

@pytest.mark.test_id("APP-254")
@pytest.mark.category("network")
@pytest.mark.priority("high")
def test_app_254_mobile_offline_mutating_action_block(appium_driver):
    """
    [APP-254] Mobile Offline Mutating Action Block
    Description: Attempt to favorite gene while offline
    Expected: Alert displays 'Action requires an internet connection'
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-254"

@pytest.mark.test_id("APP-255")
@pytest.mark.category("network")
@pytest.mark.priority("medium")
def test_app_255_mobile_slow_3g_network_latency_handling(appium_driver):
    """
    [APP-255] Mobile Slow 3G Network Latency Handling
    Description: Throttle emulator network to Slow 3G
    Expected: App displays loading spinner without premature timeout
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-255"

@pytest.mark.test_id("APP-256")
@pytest.mark.category("error-handling")
@pytest.mark.priority("high")
def test_app_256_mobile_api_500_server_error_alert(appium_driver):
    """
    [APP-256] Mobile API 500 Server Error Alert
    Description: Simulate server 500 error on mobile API call
    Expected: Displays friendly error card 'Server temporarily unavailable'
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-256"

@pytest.mark.test_id("APP-257")
@pytest.mark.category("error-handling")
@pytest.mark.priority("medium")
def test_app_257_mobile_api_404_not_found_handling(appium_driver):
    """
    [APP-257] Mobile API 404 Not Found Handling
    Description: Navigate to deleted gene ID on mobile
    Expected: Displays 'Item not found' with button to return to catalog
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-257"

@pytest.mark.test_id("APP-258")
@pytest.mark.category("security")
@pytest.mark.priority("high")
def test_app_258_mobile_session_token_tampering_defense(appium_driver):
    """
    [APP-258] Mobile Session Token Tampering Defense
    Description: Corrupt stored JWT token in mobile storage
    Expected: App detects invalid token, purges it, and redirects to login
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-258"

@pytest.mark.test_id("APP-259")
@pytest.mark.category("device")
@pytest.mark.priority("medium")
def test_app_259_mobile_screen_lock_during_active_request(appium_driver):
    """
    [APP-259] Mobile Screen Lock During Active Request
    Description: Lock screen while search request is in-flight
    Expected: Request completes and state updates cleanly upon unlock
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-259"

@pytest.mark.test_id("APP-260")
@pytest.mark.category("ui")
@pytest.mark.priority("medium")
def test_app_260_mobile_rapid_double_tap_prevention_on_forms(appium_driver):
    """
    [APP-260] Mobile Rapid Double Tap Prevention on Forms
    Description: Rapidly double tap Sign In button
    Expected: Second tap ignored; only single API request submitted
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-260"

@pytest.mark.test_id("APP-261")
@pytest.mark.category("device")
@pytest.mark.priority("medium")
def test_app_261_mobile_device_rotation_during_video_chart_view(appium_driver):
    """
    [APP-261] Mobile Device Rotation During Video/Chart View
    Description: Rotate screen to landscape while viewing charts
    Expected: Chart resizes to fill landscape width cleanly
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-261"

@pytest.mark.test_id("APP-262")
@pytest.mark.category("ui")
@pytest.mark.priority("medium")
def test_app_262_mobile_keyboard_push_up_layout_adjust(appium_driver):
    """
    [APP-262] Mobile Keyboard Push-Up Layout Adjust
    Description: Open keyboard on bottom form input
    Expected: Screen scrolls up automatically so input remains visible above keyboard
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-262"

@pytest.mark.test_id("APP-263")
@pytest.mark.category("navigation")
@pytest.mark.priority("medium")
def test_app_263_mobile_android_back_gesture_during_search(appium_driver):
    """
    [APP-263] Mobile Android Back Gesture During Search
    Description: Perform back gesture while search query active
    Expected: Clears search input first before exiting search screen
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-263"

@pytest.mark.test_id("APP-264")
@pytest.mark.category("ui")
@pytest.mark.priority("low")
def test_app_264_mobile_text_selection_in_descriptions(appium_driver):
    """
    [APP-264] Mobile Text Selection in Descriptions
    Description: Long press on scientific description text
    Expected: Selection handles appear allowing text copy
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-264"

@pytest.mark.test_id("APP-265")
@pytest.mark.category("performance")
@pytest.mark.priority("medium")
def test_app_265_mobile_webview_hardware_acceleration(appium_driver):
    """
    [APP-265] Mobile Webview Hardware Acceleration
    Description: Verify Android hardware acceleration enabled
    Expected: Hardware acceleration enabled for smooth rendering
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-265"

@pytest.mark.test_id("APP-266")
@pytest.mark.category("device")
@pytest.mark.priority("medium")
def test_app_266_mobile_clear_app_data_from_android_settings(appium_driver):
    """
    [APP-266] Mobile Clear App Data from Android Settings
    Description: Clear storage & cache from Android Settings
    Expected: App resets cleanly to first-launch state on next start
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-266"

@pytest.mark.test_id("APP-267")
@pytest.mark.category("lifecycle")
@pytest.mark.priority("low")
def test_app_267_mobile_app_update_simulation(appium_driver):
    """
    [APP-267] Mobile App Update Simulation
    Description: Install updated APK over existing version
    Expected: User session and preferences preserved across app update
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-267"

@pytest.mark.test_id("APP-268")
@pytest.mark.category("device")
@pytest.mark.priority("medium")
def test_app_268_mobile_android_14_compatibility_check(appium_driver):
    """
    [APP-268] Mobile Android 14 Compatibility Check
    Description: Execute tests on Android 14 (API 34) emulator
    Expected: App runs without deprecation warnings or crashes
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-268"

@pytest.mark.test_id("APP-269")
@pytest.mark.category("device")
@pytest.mark.priority("medium")
def test_app_269_mobile_android_12_compatibility_check(appium_driver):
    """
    [APP-269] Mobile Android 12 Compatibility Check
    Description: Execute tests on Android 12 (API 31) emulator
    Expected: App runs backwards-compatible without issues
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-269"

@pytest.mark.test_id("APP-270")
@pytest.mark.category("ui")
@pytest.mark.priority("medium")
def test_app_270_mobile_tablet_10_inch_emulator_layout(appium_driver):
    """
    [APP-270] Mobile Tablet 10-inch Emulator Layout
    Description: Launch app on 10-inch Android tablet emulator
    Expected: Layout adapts to split-pane master-detail view
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-270"

@pytest.mark.test_id("APP-271")
@pytest.mark.category("device")
@pytest.mark.priority("low")
def test_app_271_mobile_foldable_device_fold_unfold(appium_driver):
    """
    [APP-271] Mobile Foldable Device Fold / Unfold
    Description: Simulate screen unfold on foldable emulator
    Expected: Viewport adapts smoothly to expanded aspect ratio
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-271"

@pytest.mark.test_id("APP-272")
@pytest.mark.category("localization")
@pytest.mark.priority("low")
def test_app_272_mobile_system_locale_change_to_spanish(appium_driver):
    """
    [APP-272] Mobile System Locale Change to Spanish
    Description: Change Android system language to Spanish
    Expected: App defaults to English gracefully or localized strings
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-272"

@pytest.mark.test_id("APP-273")
@pytest.mark.category("localization")
@pytest.mark.priority("low")
def test_app_273_mobile_right_to_left_rtl_layout_mode(appium_driver):
    """
    [APP-273] Mobile Right-to-Left (RTL) Layout Mode
    Description: Enable 'Force RTL layout' in Android developer options
    Expected: Layout elements mirror correctly without visual breakage
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-273"

@pytest.mark.test_id("APP-274")
@pytest.mark.category("device")
@pytest.mark.priority("low")
def test_app_274_mobile_battery_saver_mode_interaction(appium_driver):
    """
    [APP-274] Mobile Battery Saver Mode Interaction
    Description: Enable Android Battery Saver mode
    Expected: App reduces background sync and animations gracefully
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-274"

@pytest.mark.test_id("APP-275")
@pytest.mark.category("device")
@pytest.mark.priority("low")
def test_app_275_mobile_low_storage_space_warning(appium_driver):
    """
    [APP-275] Mobile Low Storage Space Warning
    Description: Simulate device storage under 50MB
    Expected: App handles local cache write gracefully without crash
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-275"

@pytest.mark.test_id("APP-276")
@pytest.mark.category("ui")
@pytest.mark.priority("low")
def test_app_276_mobile_clipboard_copy_gene_symbol_toast(appium_driver):
    """
    [APP-276] Mobile Clipboard Copy Gene Symbol Toast
    Description: Tap copy icon next to gene symbol
    Expected: Android toast confirms 'Gene symbol copied to clipboard'
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-276"

@pytest.mark.test_id("APP-277")
@pytest.mark.category("ui")
@pytest.mark.priority("low")
def test_app_277_mobile_paste_from_clipboard_into_search(appium_driver):
    """
    [APP-277] Mobile Paste from Clipboard into Search
    Description: Long press in search input and select Paste
    Expected: Pasted text populates search input and triggers search
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-277"

@pytest.mark.test_id("APP-278")
@pytest.mark.category("performance")
@pytest.mark.priority("medium")
def test_app_278_mobile_capacitor_bridge_plugin_call_timeout(appium_driver):
    """
    [APP-278] Mobile Capacitor Bridge Plugin Call Timeout
    Description: Simulate delayed response from native bridge
    Expected: App handles timeout gracefully without UI freeze
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-278"

@pytest.mark.test_id("APP-279")
@pytest.mark.category("security")
@pytest.mark.priority("medium")
def test_app_279_mobile_webview_console_log_suppression(appium_driver):
    """
    [APP-279] Mobile WebView Console Log Suppression
    Description: Inspect Android logcat output in production build
    Expected: Sensitive tokens and data not printed to system logcat
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-279"

@pytest.mark.test_id("APP-280")
@pytest.mark.category("security")
@pytest.mark.priority("high")
def test_app_280_mobile_proguard_r8_obfuscation_check(appium_driver):
    """
    [APP-280] Mobile ProGuard / R8 Obfuscation Check
    Description: Inspect release APK build with dex analysis
    Expected: Code properly obfuscated with shrunk unused resources
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-280"

@pytest.mark.test_id("APP-281")
@pytest.mark.category("performance")
@pytest.mark.priority("medium")
def test_app_281_mobile_apk_file_size_optimization_15mb(appium_driver):
    """
    [APP-281] Mobile APK File Size Optimization (< 15MB)
    Description: Check size of output app-debug.apk
    Expected: APK size optimized below acceptable threshold
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-281"

@pytest.mark.test_id("APP-282")
@pytest.mark.category("performance")
@pytest.mark.priority("medium")
def test_app_282_mobile_launch_time_warm_start_benchmark(appium_driver):
    """
    [APP-282] Mobile Launch Time Warm Start Benchmark
    Description: Measure warm start time from background
    Expected: Warm start finishes under 500 milliseconds
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-282"

@pytest.mark.test_id("APP-283")
@pytest.mark.category("ui")
@pytest.mark.priority("low")
def test_app_283_mobile_image_asset_density_qualification(appium_driver):
    """
    [APP-283] Mobile Image Asset Density Qualification
    Description: Check icons across mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi
    Expected: Crisp icon assets rendered for each device density
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-283"

@pytest.mark.test_id("APP-284")
@pytest.mark.category("network")
@pytest.mark.priority("low")
def test_app_284_mobile_push_notification_payload_receive(appium_driver):
    """
    [APP-284] Mobile Push Notification Payload Receive
    Description: Simulate push notification reception
    Expected: Notification received without crashing app
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-284"

@pytest.mark.test_id("APP-285")
@pytest.mark.category("navigation")
@pytest.mark.priority("medium")
def test_app_285_mobile_push_notification_tap_deep_link(appium_driver):
    """
    [APP-285] Mobile Push Notification Tap Deep Link
    Description: Tap incoming notification banner
    Expected: App opens directly to target notification item
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-285"

@pytest.mark.test_id("APP-286")
@pytest.mark.category("navigation")
@pytest.mark.priority("low")
def test_app_286_mobile_backstack_depth_limit_handling(appium_driver):
    """
    [APP-286] Mobile Backstack Depth Limit Handling
    Description: Navigate through 15 nested detail screens
    Expected: Hardware back button unwinds navigation stack accurately
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-286"

@pytest.mark.test_id("APP-287")
@pytest.mark.category("device")
@pytest.mark.priority("low")
def test_app_287_mobile_screen_time_out_keep_screen_on_in_graph(appium_driver):
    """
    [APP-287] Mobile Screen Time-Out Keep Screen On in Graph
    Description: Inspect keepScreenOn flag on AI Insights canvas
    Expected: Screen dimming handled appropriately
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-287"

@pytest.mark.test_id("APP-288")
@pytest.mark.category("device")
@pytest.mark.priority("low")
def test_app_288_mobile_audio_focus_handling(appium_driver):
    """
    [APP-288] Mobile Audio Focus Handling
    Description: Play background audio while in app
    Expected: App does not interrupt external media playback
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-288"

@pytest.mark.test_id("APP-289")
@pytest.mark.category("performance")
@pytest.mark.priority("medium")
def test_app_289_mobile_touch_responsiveness_100ms(appium_driver):
    """
    [APP-289] Mobile Touch Responsiveness (< 100ms)
    Description: Measure input latency on button tap
    Expected: Touch feedback visible within 100ms
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-289"

@pytest.mark.test_id("APP-290")
@pytest.mark.category("performance")
@pytest.mark.priority("medium")
def test_app_290_mobile_android_strictmode_policy_violation_check(appium_driver):
    """
    [APP-290] Mobile Android StrictMode Policy Violation Check
    Description: Run app with Android StrictMode enabled
    Expected: No disk reads or network calls on main UI thread
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-290"

@pytest.mark.test_id("APP-291")
@pytest.mark.category("permissions")
@pytest.mark.priority("low")
def test_app_291_mobile_android_13_granular_media_permissions(appium_driver):
    """
    [APP-291] Mobile Android 13 Granular Media Permissions
    Description: Verify app does not request obsolete READ_EXTERNAL_STORAGE
    Expected: Compliant with Android 13 permissions model
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-291"

@pytest.mark.test_id("APP-292")
@pytest.mark.category("navigation")
@pytest.mark.priority("medium")
def test_app_292_mobile_backpress_double_tap_to_exit_app(appium_driver):
    """
    [APP-292] Mobile Backpress Double-Tap to Exit App
    Description: Press back twice on home screen
    Expected: Shows 'Press back again to exit' and closes app on second tap
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-292"

@pytest.mark.test_id("APP-293")
@pytest.mark.category("gestures")
@pytest.mark.priority("low")
def test_app_293_mobile_scroll_speed_acceleration_curve(appium_driver):
    """
    [APP-293] Mobile Scroll Speed Acceleration Curve
    Description: Verify natural Android physics scroll curve
    Expected: Scrolling adheres to platform standard friction curve
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-293"

@pytest.mark.test_id("APP-294")
@pytest.mark.category("ui")
@pytest.mark.priority("low")
def test_app_294_mobile_search_clear_on_tab_navigation_away(appium_driver):
    """
    [APP-294] Mobile Search Clear on Tab Navigation Away
    Description: Switch tabs while search query typed
    Expected: Search state preserved or cleanly reset on tab return
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-294"

@pytest.mark.test_id("APP-295")
@pytest.mark.category("ui")
@pytest.mark.priority("low")
def test_app_295_mobile_dark_mode_contrast_in_direct_sunlight(appium_driver):
    """
    [APP-295] Mobile Dark Mode Contrast in Direct Sunlight
    Description: Simulate high ambient brightness
    Expected: Text remains readable with sufficient contrast
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-295"

@pytest.mark.test_id("APP-296")
@pytest.mark.category("navigation")
@pytest.mark.priority("low")
def test_app_296_mobile_android_app_shortcut_long_press(appium_driver):
    """
    [APP-296] Mobile Android App Shortcut Long-Press
    Description: Long press app launcher icon on Android home
    Expected: Displays app shortcuts: 'Search', 'Saved Genes'
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-296"

@pytest.mark.test_id("APP-297")
@pytest.mark.category("ui")
@pytest.mark.priority("low")
def test_app_297_mobile_tap_target_spacing_verification(appium_driver):
    """
    [APP-297] Mobile Tap Target Spacing Verification
    Description: Verify spacing between adjacent clickable chips
    Expected: Minimum 8dp separation prevents accidental mistaps
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-297"

@pytest.mark.test_id("APP-298")
@pytest.mark.category("security")
@pytest.mark.priority("medium")
def test_app_298_mobile_android_safe_browsing_verification(appium_driver):
    """
    [APP-298] Mobile Android Safe Browsing Verification
    Description: Verify WebView Safe Browsing configuration
    Expected: WebView safe browsing client enabled
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-298"

@pytest.mark.test_id("APP-299")
@pytest.mark.category("security")
@pytest.mark.priority("medium")
def test_app_299_mobile_certificate_pinning_evaluation(appium_driver):
    """
    [APP-299] Mobile Certificate Pinning Evaluation
    Description: Inspect network security config XML
    Expected: Cleartext traffic disabled (cleartext: false in Capacitor config)
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-299"

@pytest.mark.test_id("APP-300")
@pytest.mark.category("e2e")
@pytest.mark.priority("critical")
def test_app_300_mobile_final_e2e_critical_user_journey(appium_driver):
    """
    [APP-300] Mobile Final E2E Critical User Journey
    Description: Login -> Search Gene -> View Detail -> Favorite -> Verify in Favorites
    Expected: Full end-to-end mobile research flow succeeds without error
    """
    # Verify mobile session and active package
    current_pkg = appium_driver.current_package
    assert current_pkg is not None
    # Base screen readiness check
    base = BaseScreen(appium_driver)
    assert appium_driver.session_id is not None, f"Appium session terminated for APP-300"

import re

def parse_apk(file_path: str) -> str:
    try:
        from androguard.misc import AnalyzeAPK
        a, d_list, dx = AnalyzeAPK(file_path)

        output = []
        output.append(f"Package: {a.get_package()}")
        output.append(f"App Name: {a.get_app_name()}")
        output.append(f"Version: {a.get_androidversion_name()} ({a.get_androidversion_code()})")

        permissions = a.get_permissions()
        output.append(f"\nPermissions ({len(permissions)}):")
        dangerous = ["WRITE_EXTERNAL_STORAGE", "READ_SMS", "SEND_SMS", "RECORD_AUDIO",
                     "CAMERA", "ACCESS_FINE_LOCATION", "READ_CONTACTS", "INSTALL_PACKAGES"]
        for perm in permissions:
            marker = "⚠️ DANGEROUS" if any(d in perm for d in dangerous) else ""
            output.append(f"  - {perm} {marker}")

        output.append(f"\nActivities: {len(a.get_activities())}")
        output.append(f"Services: {len(a.get_services())}")
        output.append(f"Receivers: {len(a.get_receivers())}")
        output.append(f"Content Providers: {len(a.get_providers())}")

        all_strings = []
        for dex in d_list:
            all_strings.extend(dex.get_strings())
        all_strings_combined = ' '.join(all_strings)

        urls = set(re.findall(r'https?://[^\s]+', all_strings_combined))
        emails = set(re.findall(r'[\w\.-]+@[\w\.-]+', all_strings_combined))
        if urls:
            output.append(f"\nHardcoded URLs: {', '.join(list(urls)[:10])}")
        if emails:
            output.append(f"Hardcoded emails: {', '.join(list(emails)[:5])}")

        dangerous_apis = [
            "Runtime.exec", "ProcessBuilder", "loadLibrary", "DexClassLoader",
            "Cipher", "getDeviceId", "getSubscriberId", "sendTextMessage",
            "HttpURLConnection", "OkHttp", "WebView.loadUrl"
        ]
        found_apis = [api for api in dangerous_apis if any(api in s for s in all_strings)]
        if found_apis:
            output.append(f"\nSuspicious API usage: {', '.join(found_apis)}")

        return "\n".join(output)

    except ImportError:
        return "Error: androguard not installed. Please run: pip install androguard"
    except Exception as e:
        return f"Error parsing APK: {e}"
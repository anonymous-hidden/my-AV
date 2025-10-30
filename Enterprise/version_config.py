# Version Configuration - ENTERPRISE VERSION
# This file determines which features are available in this build

# Version Configuration - ENTERPRISE SECURITY (Business Tier)
# Following exact user specifications for 3-tier system

VERSION_TYPE = "ENTERPRISE"
VERSION_NAME = "CyberDefense AI Enterprise"
VERSION_NUMBER = "2.1.0"

# 🏢 Enterprise Antivirus / Endpoint Security (Business Tier) Features
# Goal: Provide layered defense and centralized control across many users and devices

FEATURES = {
    "ENTERPRISE": {
        # ✅ Everything from Free Tier
        "real_time_protection": True,
        "on_demand_scanning": True,
        "automatic_updates": True,
        "basic_heuristics": True,
        "quarantine_removal": True,
        "lightweight_operation": True,
        "web_protection_basic": True,
        "email_attachment_scanning": True,
        "cloud_based_scanning": True,
        
        # ✅ Everything from Total Security Tier
        "firewall": True,
        "ransomware_protection": True,
        "webcam_protection": True,
        "microphone_protection": True,
        "anti_phishing": True,
        "anti_fraud": True,
        "parental_controls": True,
        "password_manager": True,
        "vpn": True,
        "identity_protection": True,
        "system_optimization": True,
        "safe_banking": True,
        
        # 🏢 Enterprise Features (Business Tier Only)
        "centralized_management": True,        # ✅ Deploy and manage security policies across all devices
        "edr": True,                          # ✅ Endpoint Detection & Response - advanced threat hunting
        "zero_trust_controls": True,          # ✅ Verify every user and device before granting access
        "advanced_ai_analytics": True,        # ✅ Machine learning to detect sophisticated attacks
        "data_loss_prevention": True,         # ✅ Prevent sensitive data from leaving the organization
        "network_threat_protection": True,    # ✅ Monitor and block network-based attacks
        "patch_management": True,             # ✅ Automatically update software across all endpoints
        "sandboxing": True,                   # ✅ Execute suspicious files in isolated environments
        "siem_integration": True,             # ✅ Connect with Security Information and Event Management systems
        "mobile_device_management": True,     # ✅ Secure and manage smartphones/tablets
        "compliance_reporting": True,         # ✅ Generate reports for regulatory compliance (GDPR, HIPAA, etc.)
        
        # Plan Configuration
        "premium_features": True,
        "enterprise_features": True,
        "plan_color": "#ff6b35",              # Orange for enterprise
        "plan_badge": "ENTERPRISE",
        "licensing": "Enterprise"
    }
}
# Get current tier features
def get_current_features():
    """Get features for current version type"""
    return FEATURES.get(VERSION_TYPE, FEATURES["ENTERPRISE"])

def is_feature_available(feature_name):
    """Check if a feature is available in current version"""
    current_features = get_current_features()
    return current_features.get(feature_name, False)

def get_version_info():
    """Get version information for UI display"""
    current_features = get_current_features()
    
    return {
        "type": VERSION_TYPE,
        "name": VERSION_NAME,
        "version": VERSION_NUMBER,
        "is_paid": True,
        "plan_color": current_features.get("plan_color", "#ff6b35"),
        "plan_badge": current_features.get("plan_badge", "ENTERPRISE"),
        "licensing": current_features.get("licensing", "Enterprise"),
        "premium": current_features.get("premium_features", True),
        "enterprise": current_features.get("enterprise_features", True)
    }

def get_plan_summary():
    """Get summary of current plan features"""
    return {
        "tier": "Enterprise Antivirus / Endpoint Security (Business Tier)",
        "goal": "Provide layered defense and centralized control across many users and devices",
        "includes": "Everything in Total Security, plus enterprise management and advanced analytics"
    }

# Export current version type for easy access
__all__ = ['VERSION_TYPE', 'get_version_info', 'is_feature_available', 'get_plan_summary']
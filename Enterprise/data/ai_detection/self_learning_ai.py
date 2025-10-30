"""
Self-Learning AI Cybersecurity System
Advanced AI that learns from web threat intelligence and malware samples
"""

import os
import sys
import json
import time
import requests
import threading
import hashlib
import sqlite3
import pickle
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path
import concurrent.futures
from typing import Dict, List, Any, Tuple
import logging
import asyncio
import aiohttp
import feedparser
from urllib.parse import urljoin
import re
import zipfile
import tarfile

# Machine Learning imports
try:
    from sklearn.ensemble import IsolationForest, RandomForestClassifier
    from sklearn.neural_network import MLPClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, classification_report
    import joblib
    ML_AVAILABLE = True
except ImportError:
    print("⚠️ Machine learning libraries not available. Install scikit-learn for full functionality.")
    ML_AVAILABLE = False

class SelfLearningAI:
    """Advanced self-learning AI for cybersecurity"""
    
    def __init__(self):
        self.learning_database = "ai_learning_system.db"
        self.models_directory = "ai_models"
        self.threat_feeds = []
        self.malware_sources = []
        self.learning_active = False
        self.web_scraping_active = False
        
        # AI Models
        self.pattern_recognition_model = None
        self.anomaly_detection_model = None
        self.malware_classification_model = None
        self.behavior_analysis_model = None
        
        # Learning statistics
        self.patterns_learned = 0
        self.threats_processed = 0
        self.accuracy_score = 0.0
        self.last_update = None
        
        # Threat intelligence feeds
        self.init_threat_feeds()
        
        # Initialize components
        self.init_database()
        self.init_models_directory()
        self.setup_logging()
        
        if ML_AVAILABLE:
            self.init_ml_models()
        
        print("🤖 Self-Learning AI System initialized")
    
    def init_threat_feeds(self):
        """Initialize threat intelligence feeds"""
        self.threat_feeds = [
            # Real threat intelligence feeds (be careful with these in production)
            "https://feeds.malwaredomainlist.com/files/mdl.xml",
            "https://www.malware-traffic-analysis.net/",
            "https://urlhaus.abuse.ch/downloads/text/",
            "https://feodotracker.abuse.ch/downloads/ipblocklist.txt",
            "https://sslbl.abuse.ch/blacklist/sslblacklist.csv",
            
            # CVE feeds
            "https://cve.mitre.org/data/downloads/allitems.xml",
            "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-recent.json.gz",
            
            # Malware sample sources (educational/research only)
            "https://bazaar.abuse.ch/browse/",
            "https://www.hybrid-analysis.com/",
            "https://www.virustotal.com/gui/",
            
            # Security blogs and research
            "https://krebsonsecurity.com/feed/",
            "https://threatpost.com/feed/",
            "https://www.bleepingcomputer.com/feed/",
            "https://www.darkreading.com/rss.xml"
        ]
        
        print(f"🌐 Initialized {len(self.threat_feeds)} threat intelligence feeds")
    
    def init_database(self):
        """Initialize learning database"""
        try:
            conn = sqlite3.connect(self.learning_database)
            cursor = conn.cursor()
            
            # Threat patterns table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS threat_patterns (
                    id INTEGER PRIMARY KEY,
                    pattern_hash TEXT UNIQUE,
                    pattern_type TEXT,
                    pattern_data BLOB,
                    threat_level INTEGER,
                    source TEXT,
                    first_seen DATE,
                    last_seen DATE,
                    frequency INTEGER DEFAULT 1,
                    accuracy REAL,
                    validated BOOLEAN DEFAULT 0
                )
            ''')
            
            # Malware samples table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS malware_samples (
                    id INTEGER PRIMARY KEY,
                    file_hash TEXT UNIQUE,
                    file_name TEXT,
                    file_size INTEGER,
                    malware_family TEXT,
                    behavior_patterns BLOB,
                    static_features BLOB,
                    dynamic_features BLOB,
                    detection_method TEXT,
                    confidence REAL,
                    source TEXT,
                    timestamp DATE
                )
            ''')
            
            # Learning sessions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS learning_sessions (
                    id INTEGER PRIMARY KEY,
                    session_type TEXT,
                    start_time DATE,
                    end_time DATE,
                    patterns_learned INTEGER,
                    accuracy_improvement REAL,
                    data_sources TEXT,
                    model_version TEXT
                )
            ''')
            
            # Web intelligence table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS web_intelligence (
                    id INTEGER PRIMARY KEY,
                    url TEXT,
                    content_hash TEXT,
                    threat_indicators TEXT,
                    iocs BLOB,
                    credibility_score REAL,
                    source_type TEXT,
                    scraped_date DATE,
                    processed BOOLEAN DEFAULT 0
                )
            ''')
            
            # Model performance table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS model_performance (
                    id INTEGER PRIMARY KEY,
                    model_name TEXT,
                    version TEXT,
                    accuracy REAL,
                    precision_score REAL,
                    recall REAL,
                    f1_score REAL,
                    training_samples INTEGER,
                    validation_date DATE
                )
            ''')
            
            conn.commit()
            conn.close()
            print("✅ Learning database initialized")
            
        except Exception as e:
            print(f"❌ Database initialization failed: {e}")
    
    def init_models_directory(self):
        """Initialize models directory"""
        Path(self.models_directory).mkdir(exist_ok=True)
        print(f"📁 Models directory: {self.models_directory}")
    
    def setup_logging(self):
        """Setup logging for AI learning"""
        logging.basicConfig(
            filename='ai_learning.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        print("📝 AI learning logging configured")
    
    def init_ml_models(self):
        """Initialize machine learning models"""
        try:
            # Pattern Recognition Model (Neural Network)
            self.pattern_recognition_model = MLPClassifier(
                hidden_layer_sizes=(100, 50, 25),
                activation='relu',
                solver='adam',
                max_iter=1000,
                random_state=42
            )
            
            # Anomaly Detection Model (Isolation Forest)
            self.anomaly_detection_model = IsolationForest(
                contamination=0.1,
                random_state=42
            )
            
            # Malware Classification Model (Random Forest)
            self.malware_classification_model = RandomForestClassifier(
                n_estimators=100,
                max_depth=20,
                random_state=42
            )
            
            # Behavior Analysis Model (Neural Network)
            self.behavior_analysis_model = MLPClassifier(
                hidden_layer_sizes=(150, 75, 35),
                activation='tanh',
                solver='adam',
                max_iter=1500,
                random_state=42
            )
            
            # Feature scaler
            self.feature_scaler = StandardScaler()
            
            print("🧠 Machine learning models initialized")
            
        except Exception as e:
            print(f"❌ ML model initialization failed: {e}")
    
    def start_continuous_learning(self):
        """Start continuous learning process"""
        print("🚀 Starting continuous learning system...")
        self.learning_active = True
        
        # Start learning threads
        learning_threads = [
            threading.Thread(target=self.web_intelligence_gathering, daemon=True),
            threading.Thread(target=self.threat_pattern_learning, daemon=True),
            threading.Thread(target=self.malware_sample_analysis, daemon=True),
            threading.Thread(target=self.model_retraining_loop, daemon=True),
            threading.Thread(target=self.threat_feed_monitoring, daemon=True)
        ]
        
        for thread in learning_threads:
            thread.start()
        
        print("✅ Continuous learning system started")
        return learning_threads
    
    def web_intelligence_gathering(self):
        """Gather threat intelligence from web sources"""
        while self.learning_active:
            try:
                print("🌐 Starting web intelligence gathering...")
                
                # Scrape threat feeds
                for feed_url in self.threat_feeds:
                    try:
                        self.scrape_threat_feed(feed_url)
                        time.sleep(2)  # Be respectful to servers
                    except Exception as e:
                        self.logger.error(f"Failed to scrape {feed_url}: {e}")
                
                # Process gathered intelligence
                self.process_web_intelligence()
                
                print("✅ Web intelligence gathering cycle completed")
                
                # Wait before next cycle (1 hour)
                time.sleep(3600)
                
            except Exception as e:
                self.logger.error(f"Web intelligence gathering error: {e}")
                time.sleep(300)  # Wait 5 minutes on error
    
    def scrape_threat_feed(self, url: str):
        """Scrape individual threat feed"""
        try:
            headers = {
                'User-Agent': 'CyberDefense-AI/1.0 (Security Research)',
                'Accept': 'text/html,application/xml,application/json,text/plain'
            }
            
            response = requests.get(url, headers=headers, timeout=30, verify=False)
            response.raise_for_status()
            
            # Extract threat indicators
            threat_indicators = self.extract_threat_indicators(response.text, url)
            
            if threat_indicators:
                self.store_web_intelligence(url, response.text, threat_indicators)
                print(f"📥 Extracted {len(threat_indicators)} indicators from {url}")
            
        except Exception as e:
            self.logger.warning(f"Failed to scrape {url}: {e}")
    
    def extract_threat_indicators(self, content: str, source_url: str) -> List[Dict]:
        """Extract threat indicators from content"""
        indicators = []
        
        try:
            # IP address patterns
            ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
            ips = re.findall(ip_pattern, content)
            
            for ip in ips[:50]:  # Limit to 50 IPs per source
                indicators.append({
                    'type': 'ip',
                    'value': ip,
                    'source': source_url,
                    'confidence': 0.7
                })
            
            # Domain patterns
            domain_pattern = r'\b[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]?\.[a-zA-Z]{2,}\b'
            domains = re.findall(domain_pattern, content)
            
            for domain in domains[:30]:  # Limit to 30 domains per source
                if not domain.endswith(('.com', '.org', '.net', '.gov', '.edu')):  # Skip common legitimate domains
                    indicators.append({
                        'type': 'domain',
                        'value': domain,
                        'source': source_url,
                        'confidence': 0.6
                    })
            
            # Hash patterns (MD5, SHA1, SHA256)
            hash_patterns = [
                (r'\b[a-fA-F0-9]{32}\b', 'md5'),
                (r'\b[a-fA-F0-9]{40}\b', 'sha1'),
                (r'\b[a-fA-F0-9]{64}\b', 'sha256')
            ]
            
            for pattern, hash_type in hash_patterns:
                hashes = re.findall(pattern, content)
                for hash_val in hashes[:20]:  # Limit to 20 hashes per type
                    indicators.append({
                        'type': f'hash_{hash_type}',
                        'value': hash_val,
                        'source': source_url,
                        'confidence': 0.9
                    })
            
            # URL patterns
            url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+[^\s<>"{}|\\^`\[\].,)]'
            urls = re.findall(url_pattern, content)
            
            for url in urls[:10]:  # Limit to 10 URLs per source
                indicators.append({
                    'type': 'url',
                    'value': url,
                    'source': source_url,
                    'confidence': 0.8
                })
            
        except Exception as e:
            self.logger.error(f"Failed to extract indicators: {e}")
        
        return indicators
    
    def store_web_intelligence(self, url: str, content: str, indicators: List[Dict]):
        """Store web intelligence in database"""
        try:
            conn = sqlite3.connect(self.learning_database)
            cursor = conn.cursor()
            
            content_hash = hashlib.sha256(content.encode()).hexdigest()
            
            cursor.execute('''
                INSERT OR REPLACE INTO web_intelligence 
                (url, content_hash, threat_indicators, iocs, credibility_score, source_type, scraped_date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                url,
                content_hash,
                json.dumps(indicators),
                pickle.dumps(indicators),
                self.calculate_source_credibility(url),
                self.classify_source_type(url),
                datetime.now()
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Failed to store web intelligence: {e}")
    
    def calculate_source_credibility(self, url: str) -> float:
        """Calculate credibility score for source"""
        # Simple credibility scoring based on domain
        high_credibility_domains = [
            'mitre.org', 'nist.gov', 'cve.org', 'abuse.ch',
            'malware-traffic-analysis.net', 'hybrid-analysis.com'
        ]
        
        medium_credibility_domains = [
            'virustotal.com', 'krebsonsecurity.com', 'threatpost.com',
            'bleepingcomputer.com', 'darkreading.com'
        ]
        
        for domain in high_credibility_domains:
            if domain in url.lower():
                return 0.9
        
        for domain in medium_credibility_domains:
            if domain in url.lower():
                return 0.7
        
        return 0.5  # Default credibility
    
    def classify_source_type(self, url: str) -> str:
        """Classify the type of threat intelligence source"""
        if any(x in url.lower() for x in ['cve', 'nvd', 'mitre']):
            return 'vulnerability_feed'
        elif any(x in url.lower() for x in ['malware', 'sample', 'analysis']):
            return 'malware_feed'
        elif any(x in url.lower() for x in ['blog', 'news', 'research']):
            return 'security_blog'
        elif any(x in url.lower() for x in ['feed', 'rss', 'xml']):
            return 'threat_feed'
        else:
            return 'unknown'
    
    def threat_pattern_learning(self):
        """Learn new threat patterns from gathered intelligence"""
        while self.learning_active:
            try:
                print("🧠 Starting threat pattern learning...")
                
                # Get unprocessed intelligence
                conn = sqlite3.connect(self.learning_database)
                cursor = conn.cursor()
                
                cursor.execute('''
                    SELECT id, threat_indicators, credibility_score 
                    FROM web_intelligence 
                    WHERE processed = 0 
                    LIMIT 100
                ''')
                
                unprocessed = cursor.fetchall()
                
                for intelligence_id, indicators_json, credibility in unprocessed:
                    try:
                        indicators = json.loads(indicators_json)
                        
                        # Learn patterns from indicators
                        patterns_learned = self.learn_patterns_from_indicators(indicators, credibility)
                        
                        # Mark as processed
                        cursor.execute('''
                            UPDATE web_intelligence 
                            SET processed = 1 
                            WHERE id = ?
                        ''', (intelligence_id,))
                        
                        self.patterns_learned += patterns_learned
                        
                    except Exception as e:
                        self.logger.error(f"Failed to process intelligence {intelligence_id}: {e}")
                
                conn.commit()
                conn.close()
                
                print(f"✅ Learned {self.patterns_learned} new patterns")
                
                # Wait before next learning cycle (30 minutes)
                time.sleep(1800)
                
            except Exception as e:
                self.logger.error(f"Threat pattern learning error: {e}")
                time.sleep(300)
    
    def learn_patterns_from_indicators(self, indicators: List[Dict], credibility: float) -> int:
        """Learn threat patterns from indicators"""
        patterns_count = 0
        
        try:
            conn = sqlite3.connect(self.learning_database)
            cursor = conn.cursor()
            
            for indicator in indicators:
                # Create pattern from indicator
                pattern_data = {
                    'type': indicator['type'],
                    'value': indicator['value'],
                    'features': self.extract_features_from_indicator(indicator)
                }
                
                pattern_hash = hashlib.sha256(
                    json.dumps(pattern_data, sort_keys=True).encode()
                ).hexdigest()
                
                # Calculate threat level based on type and credibility
                threat_level = self.calculate_threat_level(indicator, credibility)
                
                # Store pattern
                cursor.execute('''
                    INSERT OR IGNORE INTO threat_patterns 
                    (pattern_hash, pattern_type, pattern_data, threat_level, source, first_seen, last_seen, accuracy)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    pattern_hash,
                    indicator['type'],
                    pickle.dumps(pattern_data),
                    threat_level,
                    indicator['source'],
                    datetime.now(),
                    datetime.now(),
                    credibility
                ))
                
                # Update frequency if pattern already exists
                cursor.execute('''
                    UPDATE threat_patterns 
                    SET frequency = frequency + 1, last_seen = ? 
                    WHERE pattern_hash = ?
                ''', (datetime.now(), pattern_hash))
                
                patterns_count += 1
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Failed to learn patterns: {e}")
        
        return patterns_count
    
    def extract_features_from_indicator(self, indicator: Dict) -> List[float]:
        """Extract numerical features from threat indicator"""
        features = []
        
        try:
            indicator_type = indicator['type']
            value = indicator['value']
            
            if indicator_type == 'ip':
                # IP address features
                ip_parts = value.split('.')
                features.extend([int(part) for part in ip_parts])
                features.append(len(value))
                
            elif indicator_type == 'domain':
                # Domain features
                features.append(len(value))
                features.append(value.count('.'))
                features.append(value.count('-'))
                features.append(len(value.split('.')[0]))  # Subdomain length
                features.append(1 if any(char.isdigit() for char in value) else 0)
                
            elif indicator_type.startswith('hash_'):
                # Hash features
                features.append(len(value))
                features.append(sum(1 for c in value if c.isdigit()))
                features.append(sum(1 for c in value if c.isalpha()))
                
            elif indicator_type == 'url':
                # URL features
                features.append(len(value))
                features.append(value.count('/'))
                features.append(value.count('?'))
                features.append(value.count('&'))
                features.append(1 if 'http://' in value else 0)
                
            # Pad or truncate to fixed length (10 features)
            features = features[:10]
            while len(features) < 10:
                features.append(0.0)
                
        except Exception as e:
            self.logger.error(f"Feature extraction failed: {e}")
            features = [0.0] * 10
        
        return features
    
    def calculate_threat_level(self, indicator: Dict, credibility: float) -> int:
        """Calculate threat level for indicator"""
        base_scores = {
            'ip': 6,
            'domain': 5,
            'hash_md5': 8,
            'hash_sha1': 8,
            'hash_sha256': 9,
            'url': 7
        }
        
        base_score = base_scores.get(indicator['type'], 5)
        confidence = indicator.get('confidence', 0.5)
        
        # Calculate final threat level (1-10)
        threat_level = int(base_score * credibility * confidence)
        return max(1, min(10, threat_level))
    
    def malware_sample_analysis(self):
        """Analyze malware samples for learning"""
        while self.learning_active:
            try:
                print("🦠 Starting malware sample analysis...")
                
                # In a real implementation, this would analyze actual malware samples
                # For safety, we'll simulate the analysis
                self.simulate_malware_analysis()
                
                print("✅ Malware analysis cycle completed")
                
                # Wait before next analysis cycle (2 hours)
                time.sleep(7200)
                
            except Exception as e:
                self.logger.error(f"Malware analysis error: {e}")
                time.sleep(600)
    
    def simulate_malware_analysis(self):
        """Simulate malware sample analysis for learning"""
        # Simulated malware families for training
        malware_families = [
            'trojan.generic', 'ransomware.wannacry', 'botnet.mirai',
            'spyware.keylogger', 'adware.generic', 'rootkit.stuxnet',
            'worm.conficker', 'backdoor.rat', 'cryptominer.generic'
        ]
        
        try:
            conn = sqlite3.connect(self.learning_database)
            cursor = conn.cursor()
            
            for _ in range(10):  # Simulate 10 samples per cycle
                # Generate simulated sample data
                sample_hash = hashlib.sha256(
                    f"sample_{datetime.now()}_{np.random.randint(1000000)}".encode()
                ).hexdigest()
                
                malware_family = np.random.choice(malware_families)
                
                # Simulated behavioral patterns
                behavior_patterns = {
                    'file_operations': np.random.randint(0, 100),
                    'network_connections': np.random.randint(0, 50),
                    'registry_modifications': np.random.randint(0, 200),
                    'process_injections': np.random.randint(0, 10),
                    'api_calls': np.random.randint(100, 1000)
                }
                
                # Simulated static features
                static_features = {
                    'file_size': np.random.randint(1024, 10485760),
                    'entropy': np.random.uniform(0.1, 8.0),
                    'pe_sections': np.random.randint(3, 15),
                    'imports_count': np.random.randint(10, 200),
                    'exports_count': np.random.randint(0, 50)
                }
                
                # Store sample
                cursor.execute('''
                    INSERT OR IGNORE INTO malware_samples 
                    (file_hash, file_name, file_size, malware_family, behavior_patterns, 
                     static_features, detection_method, confidence, source, timestamp)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    sample_hash,
                    f"sample_{np.random.randint(1000)}.exe",
                    static_features['file_size'],
                    malware_family,
                    pickle.dumps(behavior_patterns),
                    pickle.dumps(static_features),
                    'simulated_analysis',
                    np.random.uniform(0.8, 0.99),
                    'simulation',
                    datetime.now()
                ))
            
            conn.commit()
            conn.close()
            
            print("📊 Simulated malware samples stored for learning")
            
        except Exception as e:
            self.logger.error(f"Malware simulation failed: {e}")
    
    def model_retraining_loop(self):
        """Continuously retrain models with new data"""
        while self.learning_active:
            try:
                print("🔄 Starting model retraining...")
                
                if ML_AVAILABLE:
                    # Retrain pattern recognition model
                    self.retrain_pattern_recognition_model()
                    
                    # Retrain malware classification model
                    self.retrain_malware_classification_model()
                    
                    # Retrain anomaly detection model
                    self.retrain_anomaly_detection_model()
                    
                    # Save models
                    self.save_trained_models()
                    
                    print("✅ Model retraining completed")
                else:
                    print("⚠️ ML libraries not available, skipping model retraining")
                
                # Wait before next retraining cycle (6 hours)
                time.sleep(21600)
                
            except Exception as e:
                self.logger.error(f"Model retraining error: {e}")
                time.sleep(1800)  # Wait 30 minutes on error
    
    def retrain_pattern_recognition_model(self):
        """Retrain pattern recognition model"""
        try:
            conn = sqlite3.connect(self.learning_database)
            cursor = conn.cursor()
            
            # Get training data
            cursor.execute('''
                SELECT pattern_data, threat_level 
                FROM threat_patterns 
                WHERE accuracy > 0.7
                LIMIT 1000
            ''')
            
            training_data = cursor.fetchall()
            
            if len(training_data) < 50:
                print("⚠️ Insufficient training data for pattern recognition")
                return
            
            # Prepare features and labels
            X = []
            y = []
            
            for pattern_blob, threat_level in training_data:
                try:
                    pattern_data = pickle.loads(pattern_blob)
                    features = pattern_data.get('features', [0.0] * 10)
                    X.append(features)
                    y.append(threat_level)
                except Exception as e:
                    continue
            
            if len(X) < 50:
                print("⚠️ Insufficient valid training samples")
                return
            
            X = np.array(X)
            y = np.array(y)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Scale features
            X_train_scaled = self.feature_scaler.fit_transform(X_train)
            X_test_scaled = self.feature_scaler.transform(X_test)
            
            # Train model
            self.pattern_recognition_model.fit(X_train_scaled, y_train)
            
            # Evaluate
            y_pred = self.pattern_recognition_model.predict(X_test_scaled)
            accuracy = accuracy_score(y_test, y_pred)
            
            self.accuracy_score = accuracy
            
            # Store performance
            cursor.execute('''
                INSERT INTO model_performance 
                (model_name, version, accuracy, training_samples, validation_date)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                'pattern_recognition',
                '1.0',
                accuracy,
                len(X_train),
                datetime.now()
            ))
            
            conn.commit()
            conn.close()
            
            print(f"🧠 Pattern recognition model retrained - Accuracy: {accuracy:.3f}")
            
        except Exception as e:
            self.logger.error(f"Pattern recognition retraining failed: {e}")
    
    def retrain_malware_classification_model(self):
        """Retrain malware classification model"""
        try:
            conn = sqlite3.connect(self.learning_database)
            cursor = conn.cursor()
            
            # Get malware training data
            cursor.execute('''
                SELECT static_features, behavior_patterns, malware_family 
                FROM malware_samples 
                WHERE confidence > 0.8
                LIMIT 1000
            ''')
            
            training_data = cursor.fetchall()
            
            if len(training_data) < 50:
                print("⚠️ Insufficient malware training data")
                return
            
            # Prepare features and labels
            X = []
            y = []
            
            for static_blob, behavior_blob, family in training_data:
                try:
                    static_features = pickle.loads(static_blob)
                    behavior_features = pickle.loads(behavior_blob)
                    
                    # Combine features
                    combined_features = [
                        static_features.get('file_size', 0),
                        static_features.get('entropy', 0),
                        static_features.get('pe_sections', 0),
                        static_features.get('imports_count', 0),
                        static_features.get('exports_count', 0),
                        behavior_features.get('file_operations', 0),
                        behavior_features.get('network_connections', 0),
                        behavior_features.get('registry_modifications', 0),
                        behavior_features.get('process_injections', 0),
                        behavior_features.get('api_calls', 0)
                    ]
                    
                    X.append(combined_features)
                    y.append(family)
                    
                except Exception as e:
                    continue
            
            if len(X) < 50:
                print("⚠️ Insufficient valid malware samples")
                return
            
            X = np.array(X)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Train model
            self.malware_classification_model.fit(X_train, y_train)
            
            # Evaluate
            y_pred = self.malware_classification_model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            
            print(f"🦠 Malware classification model retrained - Accuracy: {accuracy:.3f}")
            
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Malware classification retraining failed: {e}")
    
    def retrain_anomaly_detection_model(self):
        """Retrain anomaly detection model"""
        try:
            # Generate normal behavior baseline from system patterns
            normal_patterns = []
            
            for _ in range(500):  # Generate 500 normal patterns
                pattern = [
                    np.random.normal(50, 10),    # CPU usage
                    np.random.normal(60, 15),    # Memory usage
                    np.random.normal(100, 30),   # Network activity
                    np.random.normal(20, 5),     # Process count
                    np.random.normal(5, 2),      # File operations
                    np.random.normal(10, 3),     # Registry operations
                    np.random.normal(2, 1),      # Service changes
                    np.random.normal(15, 5),     # Network connections
                    np.random.normal(0, 0.5),    # Privilege escalations
                    np.random.normal(1, 0.3)     # Suspicious API calls
                ]
                normal_patterns.append(pattern)
            
            X_normal = np.array(normal_patterns)
            
            # Train anomaly detection model
            self.anomaly_detection_model.fit(X_normal)
            
            print("🔍 Anomaly detection model retrained")
            
        except Exception as e:
            self.logger.error(f"Anomaly detection retraining failed: {e}")
    
    def save_trained_models(self):
        """Save trained models to disk"""
        try:
            model_files = {
                'pattern_recognition': self.pattern_recognition_model,
                'malware_classification': self.malware_classification_model,
                'anomaly_detection': self.anomaly_detection_model,
                'feature_scaler': self.feature_scaler
            }
            
            for name, model in model_files.items():
                if model is not None:
                    model_path = os.path.join(self.models_directory, f"{name}_model.pkl")
                    joblib.dump(model, model_path)
            
            self.last_update = datetime.now()
            print(f"💾 Models saved to {self.models_directory}")
            
        except Exception as e:
            self.logger.error(f"Model saving failed: {e}")
    
    def threat_feed_monitoring(self):
        """Monitor threat feeds for new threats"""
        while self.learning_active:
            try:
                print("📡 Monitoring threat feeds...")
                
                # Check RSS/XML feeds
                for feed_url in self.threat_feeds:
                    if any(ext in feed_url.lower() for ext in ['.xml', '.rss', 'feed']):
                        try:
                            self.parse_threat_feed(feed_url)
                        except Exception as e:
                            self.logger.warning(f"Failed to parse feed {feed_url}: {e}")
                
                print("✅ Threat feed monitoring cycle completed")
                
                # Wait before next monitoring cycle (2 hours)
                time.sleep(7200)
                
            except Exception as e:
                self.logger.error(f"Threat feed monitoring error: {e}")
                time.sleep(600)
    
    def parse_threat_feed(self, feed_url: str):
        """Parse RSS/XML threat feed"""
        try:
            feed = feedparser.parse(feed_url)
            
            for entry in feed.entries[:10]:  # Limit to 10 entries per feed
                title = entry.get('title', '')
                description = entry.get('description', '')
                link = entry.get('link', '')
                
                # Extract threat information
                threat_info = {
                    'title': title,
                    'description': description,
                    'link': link,
                    'source': feed_url,
                    'published': entry.get('published', ''),
                    'threat_indicators': self.extract_threat_indicators(
                        f"{title} {description}", feed_url
                    )
                }
                
                # Store threat information
                if threat_info['threat_indicators']:
                    self.store_threat_feed_data(threat_info)
            
        except Exception as e:
            self.logger.error(f"Failed to parse threat feed {feed_url}: {e}")
    
    def store_threat_feed_data(self, threat_info: Dict):
        """Store threat feed data"""
        try:
            conn = sqlite3.connect(self.learning_database)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT OR IGNORE INTO web_intelligence 
                (url, content_hash, threat_indicators, credibility_score, source_type, scraped_date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                threat_info['link'],
                hashlib.sha256(threat_info['description'].encode()).hexdigest(),
                json.dumps(threat_info['threat_indicators']),
                0.8,  # High credibility for threat feeds
                'threat_feed',
                datetime.now()
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Failed to store threat feed data: {e}")
    
    def get_learning_status(self) -> Dict:
        """Get current learning status"""
        try:
            conn = sqlite3.connect(self.learning_database)
            cursor = conn.cursor()
            
            # Count patterns
            cursor.execute("SELECT COUNT(*) FROM threat_patterns")
            total_patterns = cursor.fetchone()[0]
            
            # Count malware samples
            cursor.execute("SELECT COUNT(*) FROM malware_samples")
            total_samples = cursor.fetchone()[0]
            
            # Count web intelligence
            cursor.execute("SELECT COUNT(*) FROM web_intelligence")
            total_intelligence = cursor.fetchone()[0]
            
            # Get latest model performance
            cursor.execute('''
                SELECT accuracy FROM model_performance 
                WHERE model_name = 'pattern_recognition' 
                ORDER BY validation_date DESC LIMIT 1
            ''')
            
            latest_accuracy = cursor.fetchone()
            model_accuracy = latest_accuracy[0] if latest_accuracy else 0.0
            
            conn.close()
            
            return {
                'learning_active': self.learning_active,
                'total_patterns': total_patterns,
                'total_samples': total_samples,
                'total_intelligence': total_intelligence,
                'model_accuracy': model_accuracy,
                'patterns_learned': self.patterns_learned,
                'threats_processed': self.threats_processed,
                'last_update': self.last_update.isoformat() if self.last_update else None,
                'ml_available': ML_AVAILABLE
            }
            
        except Exception as e:
            self.logger.error(f"Failed to get learning status: {e}")
            return {'error': str(e)}
    
    def stop_learning(self):
        """Stop the learning process"""
        self.learning_active = False
        print("🛑 Self-learning AI system stopped")
    
    def predict_threat(self, features: List[float]) -> Dict:
        """Predict if given features represent a threat"""
        if not ML_AVAILABLE or self.pattern_recognition_model is None:
            return {'error': 'ML models not available'}
        
        try:
            # Scale features
            features_scaled = self.feature_scaler.transform([features])
            
            # Predict threat level
            threat_level = self.pattern_recognition_model.predict(features_scaled)[0]
            
            # Predict anomaly
            anomaly_score = self.anomaly_detection_model.decision_function(features_scaled)[0]
            is_anomaly = self.anomaly_detection_model.predict(features_scaled)[0] == -1
            
            return {
                'threat_level': int(threat_level),
                'anomaly_score': float(anomaly_score),
                'is_anomaly': bool(is_anomaly),
                'confidence': self.accuracy_score
            }
            
        except Exception as e:
            return {'error': str(e)}

def main():
    """Main function for self-learning AI"""
    print("🤖 CyberDefense AI - Self-Learning System")
    print("Advanced AI that learns from web threat intelligence")
    print("-" * 60)
    
    ai_system = SelfLearningAI()
    
    try:
        # Start continuous learning
        learning_threads = ai_system.start_continuous_learning()
        
        print("\n✅ Self-learning AI system is running!")
        print("The AI is now continuously learning from web sources...")
        print("Press Ctrl+C to stop")
        
        # Keep main thread alive
        while ai_system.learning_active:
            status = ai_system.get_learning_status()
            
            print(f"\n📊 Learning Status:")
            print(f"   🧠 Patterns Learned: {status.get('total_patterns', 0)}")
            print(f"   🦠 Malware Samples: {status.get('total_samples', 0)}")
            print(f"   🌐 Intelligence Gathered: {status.get('total_intelligence', 0)}")
            print(f"   🎯 Model Accuracy: {status.get('model_accuracy', 0):.3f}")
            
            time.sleep(30)  # Update status every 30 seconds
        
    except KeyboardInterrupt:
        print("\n🛑 Stopping self-learning AI system...")
        ai_system.stop_learning()
    except Exception as e:
        print(f"\n❌ AI system error: {e}")
        ai_system.stop_learning()

if __name__ == "__main__":
    main()
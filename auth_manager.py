import json
import hashlib
import os
from datetime import datetime

class AuthManager:
    def __init__(self, users_file="users.json"):
        self.users_file = users_file
        self.users = {}
        self.load_users()
        self.initialize_admin()
    
    def load_users(self):
        """Load users from JSON file"""
        try:
            if os.path.exists(self.users_file):
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    self.users = json.load(f)
            else:
                self.users = {}
        except Exception as e:
            print(f"Error loading users: {e}")
            self.users = {}
    
    def save_users(self):
        """Save users to JSON file"""
        try:
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump(self.users, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving users: {e}")
    
    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def initialize_admin(self):
        """Create default admin account"""
        if 'admin' not in self.users:
            self.users['admin'] = {
                'password': self.hash_password('admin'),
                'role': 'admin',
                'created_at': datetime.now().isoformat(),
                'email': 'admin@filemanager.com'
            }
            self.save_users()
    
    def login(self, username, password):
        """Authenticate user"""
        if username in self.users:
            stored_hash = self.users[username]['password']
            if stored_hash == self.hash_password(password):
                return {
                    'success': True,
                    'username': username,
                    'role': self.users[username]['role']
                }
        return {'success': False, 'error': 'Invalid username or password'}
    
    def register(self, username, password, email=""):
        """Register new user"""
        if username in self.users:
            return {'success': False, 'error': 'Username already exists'}
        
        if len(password) < 4:
            return {'success': False, 'error': 'Password must be at least 4 characters'}
        
        self.users[username] = {
            'password': self.hash_password(password),
            'role': 'user',
            'created_at': datetime.now().isoformat(),
            'email': email
        }
        self.save_users()
        return {'success': True, 'message': 'User registered successfully'}
    
    def get_all_users(self):
        """Get all users (admin only)"""
        return list(self.users.keys())
    
    def delete_user(self, username):
        """Delete a user (admin only)"""
        if username == 'admin':
            return {'success': False, 'error': 'Cannot delete admin account'}
        
        if username in self.users:
            del self.users[username]
            self.save_users()
            return {'success': True, 'message': f'User {username} deleted'}
        
        return {'success': False, 'error': 'User not found'}
    
    def change_password(self, username, old_password, new_password):
        """Change user password"""
        if username not in self.users:
            return {'success': False, 'error': 'User not found'}
        
        stored_hash = self.users[username]['password']
        if stored_hash != self.hash_password(old_password):
            return {'success': False, 'error': 'Old password is incorrect'}
        
        if len(new_password) < 4:
            return {'success': False, 'error': 'New password must be at least 4 characters'}
        
        self.users[username]['password'] = self.hash_password(new_password)
        self.save_users()
        return {'success': True, 'message': 'Password changed successfully'}
    
    def get_user_info(self, username):
        """Get user information"""
        if username in self.users:
            user = self.users[username].copy()
            user.pop('password', None)
            return user
        return None
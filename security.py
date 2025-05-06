# Copyright (c) 2025 Neil Archer@hotmail.com. All rights reserved.

import pyotp

class Security:
    def __init__(self):
        self.mfa_secret = 'YOUR_MFA_SECRET'  # Secret for MFA

    def generate_mfa_token(self):
        totp = pyotp.TOTP(self.mfa_secret)
        return totp.now()

    def verify_mfa_token(self, token):
        totp = pyotp.TOTP(self.mfa_secret)
        return totp.verify(token)

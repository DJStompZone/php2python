#!/usr/bin/env python3
# coding: utf-8
if '__PHP2PY_LOADED__' not in globals():
    import os
    with open(os.getenv('PHP2PY_COMPAT', 'php_compat.py')) as f:
        exec(compile(f.read(), '<string>', 'exec'))
    # end with
    globals()['__PHP2PY_LOADED__'] = True
# end if
if php_class_exists("ParagonIE_Sodium_Crypto32", False):
    sys.exit(-1)
# end if
#// 
#// Class ParagonIE_Sodium_Crypto
#// 
#// ATTENTION!
#// 
#// If you are using this library, you should be using
#// ParagonIE_Sodium_Compat in your code, not this class.
#//
class ParagonIE_Sodium_Crypto32():
    aead_chacha20poly1305_KEYBYTES = 32
    aead_chacha20poly1305_NSECBYTES = 0
    aead_chacha20poly1305_NPUBBYTES = 8
    aead_chacha20poly1305_ABYTES = 16
    aead_chacha20poly1305_IETF_KEYBYTES = 32
    aead_chacha20poly1305_IETF_NSECBYTES = 0
    aead_chacha20poly1305_IETF_NPUBBYTES = 12
    aead_chacha20poly1305_IETF_ABYTES = 16
    aead_xchacha20poly1305_IETF_KEYBYTES = 32
    aead_xchacha20poly1305_IETF_NSECBYTES = 0
    aead_xchacha20poly1305_IETF_NPUBBYTES = 24
    aead_xchacha20poly1305_IETF_ABYTES = 16
    box_curve25519xsalsa20poly1305_SEEDBYTES = 32
    box_curve25519xsalsa20poly1305_PUBLICKEYBYTES = 32
    box_curve25519xsalsa20poly1305_SECRETKEYBYTES = 32
    box_curve25519xsalsa20poly1305_BEFORENMBYTES = 32
    box_curve25519xsalsa20poly1305_NONCEBYTES = 24
    box_curve25519xsalsa20poly1305_MACBYTES = 16
    box_curve25519xsalsa20poly1305_BOXZEROBYTES = 16
    box_curve25519xsalsa20poly1305_ZEROBYTES = 32
    onetimeauth_poly1305_BYTES = 16
    onetimeauth_poly1305_KEYBYTES = 32
    secretbox_xsalsa20poly1305_KEYBYTES = 32
    secretbox_xsalsa20poly1305_NONCEBYTES = 24
    secretbox_xsalsa20poly1305_MACBYTES = 16
    secretbox_xsalsa20poly1305_BOXZEROBYTES = 16
    secretbox_xsalsa20poly1305_ZEROBYTES = 32
    secretbox_xchacha20poly1305_KEYBYTES = 32
    secretbox_xchacha20poly1305_NONCEBYTES = 24
    secretbox_xchacha20poly1305_MACBYTES = 16
    secretbox_xchacha20poly1305_BOXZEROBYTES = 16
    secretbox_xchacha20poly1305_ZEROBYTES = 32
    stream_salsa20_KEYBYTES = 32
    #// 
    #// AEAD Decryption with ChaCha20-Poly1305
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $message
    #// @param string $ad
    #// @param string $nonce
    #// @param string $key
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def aead_chacha20poly1305_decrypt(self, message_="", ad_="", nonce_="", key_=""):
        
        
        #// @var int $len - Length of message (ciphertext + MAC)
        len_ = ParagonIE_Sodium_Core32_Util.strlen(message_)
        #// @var int  $clen - Length of ciphertext
        clen_ = len_ - self.aead_chacha20poly1305_ABYTES
        #// @var int $adlen - Length of associated data
        adlen_ = ParagonIE_Sodium_Core32_Util.strlen(ad_)
        #// @var string $mac - Message authentication code
        mac_ = ParagonIE_Sodium_Core32_Util.substr(message_, clen_, self.aead_chacha20poly1305_ABYTES)
        #// @var string $ciphertext - The encrypted message (sans MAC)
        ciphertext_ = ParagonIE_Sodium_Core32_Util.substr(message_, 0, clen_)
        #// @var string The first block of the chacha20 keystream, used as a poly1305 key
        block0_ = ParagonIE_Sodium_Core32_ChaCha20.stream(32, nonce_, key_)
        #// Recalculate the Poly1305 authentication tag (MAC):
        state_ = php_new_class("ParagonIE_Sodium_Core32_Poly1305_State", lambda : ParagonIE_Sodium_Core32_Poly1305_State(block0_))
        try: 
            ParagonIE_Sodium_Compat.memzero(block0_)
        except SodiumException as ex_:
            block0_ = None
        # end try
        state_.update(ad_)
        state_.update(ParagonIE_Sodium_Core32_Util.store64_le(adlen_))
        state_.update(ciphertext_)
        state_.update(ParagonIE_Sodium_Core32_Util.store64_le(clen_))
        computed_mac_ = state_.finish()
        #// Compare the given MAC with the recalculated MAC:
        if (not ParagonIE_Sodium_Core32_Util.verify_16(computed_mac_, mac_)):
            raise php_new_class("SodiumException", lambda : SodiumException("Invalid MAC"))
        # end if
        #// Here, we know that the MAC is valid, so we decrypt and return the plaintext
        return ParagonIE_Sodium_Core32_ChaCha20.streamxoric(ciphertext_, nonce_, key_, ParagonIE_Sodium_Core32_Util.store64_le(1))
    # end def aead_chacha20poly1305_decrypt
    #// 
    #// AEAD Encryption with ChaCha20-Poly1305
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $message
    #// @param string $ad
    #// @param string $nonce
    #// @param string $key
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def aead_chacha20poly1305_encrypt(self, message_="", ad_="", nonce_="", key_=""):
        
        
        #// @var int $len - Length of the plaintext message
        len_ = ParagonIE_Sodium_Core32_Util.strlen(message_)
        #// @var int $adlen - Length of the associated data
        adlen_ = ParagonIE_Sodium_Core32_Util.strlen(ad_)
        #// @var string The first block of the chacha20 keystream, used as a poly1305 key
        block0_ = ParagonIE_Sodium_Core32_ChaCha20.stream(32, nonce_, key_)
        state_ = php_new_class("ParagonIE_Sodium_Core32_Poly1305_State", lambda : ParagonIE_Sodium_Core32_Poly1305_State(block0_))
        try: 
            ParagonIE_Sodium_Compat.memzero(block0_)
        except SodiumException as ex_:
            block0_ = None
        # end try
        #// @var string $ciphertext - Raw encrypted data
        ciphertext_ = ParagonIE_Sodium_Core32_ChaCha20.streamxoric(message_, nonce_, key_, ParagonIE_Sodium_Core32_Util.store64_le(1))
        state_.update(ad_)
        state_.update(ParagonIE_Sodium_Core32_Util.store64_le(adlen_))
        state_.update(ciphertext_)
        state_.update(ParagonIE_Sodium_Core32_Util.store64_le(len_))
        return ciphertext_ + state_.finish()
    # end def aead_chacha20poly1305_encrypt
    #// 
    #// AEAD Decryption with ChaCha20-Poly1305, IETF mode (96-bit nonce)
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $message
    #// @param string $ad
    #// @param string $nonce
    #// @param string $key
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def aead_chacha20poly1305_ietf_decrypt(self, message_="", ad_="", nonce_="", key_=""):
        
        
        #// @var int $adlen - Length of associated data
        adlen_ = ParagonIE_Sodium_Core32_Util.strlen(ad_)
        #// @var int $len - Length of message (ciphertext + MAC)
        len_ = ParagonIE_Sodium_Core32_Util.strlen(message_)
        #// @var int  $clen - Length of ciphertext
        clen_ = len_ - self.aead_chacha20poly1305_IETF_ABYTES
        #// @var string The first block of the chacha20 keystream, used as a poly1305 key
        block0_ = ParagonIE_Sodium_Core32_ChaCha20.ietfstream(32, nonce_, key_)
        #// @var string $mac - Message authentication code
        mac_ = ParagonIE_Sodium_Core32_Util.substr(message_, len_ - self.aead_chacha20poly1305_IETF_ABYTES, self.aead_chacha20poly1305_IETF_ABYTES)
        #// @var string $ciphertext - The encrypted message (sans MAC)
        ciphertext_ = ParagonIE_Sodium_Core32_Util.substr(message_, 0, len_ - self.aead_chacha20poly1305_IETF_ABYTES)
        #// Recalculate the Poly1305 authentication tag (MAC):
        state_ = php_new_class("ParagonIE_Sodium_Core32_Poly1305_State", lambda : ParagonIE_Sodium_Core32_Poly1305_State(block0_))
        try: 
            ParagonIE_Sodium_Compat.memzero(block0_)
        except SodiumException as ex_:
            block0_ = None
        # end try
        state_.update(ad_)
        state_.update(php_str_repeat(" ", 16 - adlen_ & 15))
        state_.update(ciphertext_)
        state_.update(php_str_repeat(" ", 16 - clen_ & 15))
        state_.update(ParagonIE_Sodium_Core32_Util.store64_le(adlen_))
        state_.update(ParagonIE_Sodium_Core32_Util.store64_le(clen_))
        computed_mac_ = state_.finish()
        #// Compare the given MAC with the recalculated MAC:
        if (not ParagonIE_Sodium_Core32_Util.verify_16(computed_mac_, mac_)):
            raise php_new_class("SodiumException", lambda : SodiumException("Invalid MAC"))
        # end if
        #// Here, we know that the MAC is valid, so we decrypt and return the plaintext
        return ParagonIE_Sodium_Core32_ChaCha20.ietfstreamxoric(ciphertext_, nonce_, key_, ParagonIE_Sodium_Core32_Util.store64_le(1))
    # end def aead_chacha20poly1305_ietf_decrypt
    #// 
    #// AEAD Encryption with ChaCha20-Poly1305, IETF mode (96-bit nonce)
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $message
    #// @param string $ad
    #// @param string $nonce
    #// @param string $key
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def aead_chacha20poly1305_ietf_encrypt(self, message_="", ad_="", nonce_="", key_=""):
        
        
        #// @var int $len - Length of the plaintext message
        len_ = ParagonIE_Sodium_Core32_Util.strlen(message_)
        #// @var int $adlen - Length of the associated data
        adlen_ = ParagonIE_Sodium_Core32_Util.strlen(ad_)
        #// @var string The first block of the chacha20 keystream, used as a poly1305 key
        block0_ = ParagonIE_Sodium_Core32_ChaCha20.ietfstream(32, nonce_, key_)
        state_ = php_new_class("ParagonIE_Sodium_Core32_Poly1305_State", lambda : ParagonIE_Sodium_Core32_Poly1305_State(block0_))
        try: 
            ParagonIE_Sodium_Compat.memzero(block0_)
        except SodiumException as ex_:
            block0_ = None
        # end try
        #// @var string $ciphertext - Raw encrypted data
        ciphertext_ = ParagonIE_Sodium_Core32_ChaCha20.ietfstreamxoric(message_, nonce_, key_, ParagonIE_Sodium_Core32_Util.store64_le(1))
        state_.update(ad_)
        state_.update(php_str_repeat(" ", 16 - adlen_ & 15))
        state_.update(ciphertext_)
        state_.update(php_str_repeat(" ", 16 - len_ & 15))
        state_.update(ParagonIE_Sodium_Core32_Util.store64_le(adlen_))
        state_.update(ParagonIE_Sodium_Core32_Util.store64_le(len_))
        return ciphertext_ + state_.finish()
    # end def aead_chacha20poly1305_ietf_encrypt
    #// 
    #// AEAD Decryption with ChaCha20-Poly1305, IETF mode (96-bit nonce)
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $message
    #// @param string $ad
    #// @param string $nonce
    #// @param string $key
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def aead_xchacha20poly1305_ietf_decrypt(self, message_="", ad_="", nonce_="", key_=""):
        
        
        subkey_ = ParagonIE_Sodium_Core32_HChaCha20.hchacha20(ParagonIE_Sodium_Core32_Util.substr(nonce_, 0, 16), key_)
        nonceLast_ = "    " + ParagonIE_Sodium_Core32_Util.substr(nonce_, 16, 8)
        return self.aead_chacha20poly1305_ietf_decrypt(message_, ad_, nonceLast_, subkey_)
    # end def aead_xchacha20poly1305_ietf_decrypt
    #// 
    #// AEAD Encryption with ChaCha20-Poly1305, IETF mode (96-bit nonce)
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $message
    #// @param string $ad
    #// @param string $nonce
    #// @param string $key
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def aead_xchacha20poly1305_ietf_encrypt(self, message_="", ad_="", nonce_="", key_=""):
        
        
        subkey_ = ParagonIE_Sodium_Core32_HChaCha20.hchacha20(ParagonIE_Sodium_Core32_Util.substr(nonce_, 0, 16), key_)
        nonceLast_ = "    " + ParagonIE_Sodium_Core32_Util.substr(nonce_, 16, 8)
        return self.aead_chacha20poly1305_ietf_encrypt(message_, ad_, nonceLast_, subkey_)
    # end def aead_xchacha20poly1305_ietf_encrypt
    #// 
    #// HMAC-SHA-512-256 (a.k.a. the leftmost 256 bits of HMAC-SHA-512)
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $message
    #// @param string $key
    #// @return string
    #// @throws TypeError
    #//
    @classmethod
    def auth(self, message_=None, key_=None):
        
        
        return ParagonIE_Sodium_Core32_Util.substr(php_hash_hmac("sha512", message_, key_, True), 0, 32)
    # end def auth
    #// 
    #// HMAC-SHA-512-256 validation. Constant-time via hash_equals().
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $mac
    #// @param string $message
    #// @param string $key
    #// @return bool
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def auth_verify(self, mac_=None, message_=None, key_=None):
        
        
        return ParagonIE_Sodium_Core32_Util.hashequals(mac_, self.auth(message_, key_))
    # end def auth_verify
    #// 
    #// X25519 key exchange followed by XSalsa20Poly1305 symmetric encryption
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $plaintext
    #// @param string $nonce
    #// @param string $keypair
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def box(self, plaintext_=None, nonce_=None, keypair_=None):
        
        
        return self.secretbox(plaintext_, nonce_, self.box_beforenm(self.box_secretkey(keypair_), self.box_publickey(keypair_)))
    # end def box
    #// 
    #// X25519-XSalsa20-Poly1305 with one ephemeral X25519 keypair.
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $message
    #// @param string $publicKey
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def box_seal(self, message_=None, publicKey_=None):
        
        
        #// @var string $ephemeralKeypair
        ephemeralKeypair_ = self.box_keypair()
        #// @var string $ephemeralSK
        ephemeralSK_ = self.box_secretkey(ephemeralKeypair_)
        #// @var string $ephemeralPK
        ephemeralPK_ = self.box_publickey(ephemeralKeypair_)
        #// @var string $nonce
        nonce_ = self.generichash(ephemeralPK_ + publicKey_, "", 24)
        #// @var string $keypair - The combined keypair used in crypto_box()
        keypair_ = self.box_keypair_from_secretkey_and_publickey(ephemeralSK_, publicKey_)
        #// @var string $ciphertext Ciphertext + MAC from crypto_box
        ciphertext_ = self.box(message_, nonce_, keypair_)
        try: 
            ParagonIE_Sodium_Compat.memzero(ephemeralKeypair_)
            ParagonIE_Sodium_Compat.memzero(ephemeralSK_)
            ParagonIE_Sodium_Compat.memzero(nonce_)
        except SodiumException as ex_:
            ephemeralKeypair_ = None
            ephemeralSK_ = None
            nonce_ = None
        # end try
        return ephemeralPK_ + ciphertext_
    # end def box_seal
    #// 
    #// Opens a message encrypted via box_seal().
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $message
    #// @param string $keypair
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def box_seal_open(self, message_=None, keypair_=None):
        
        
        #// @var string $ephemeralPK
        ephemeralPK_ = ParagonIE_Sodium_Core32_Util.substr(message_, 0, 32)
        #// @var string $ciphertext (ciphertext + MAC)
        ciphertext_ = ParagonIE_Sodium_Core32_Util.substr(message_, 32)
        #// @var string $secretKey
        secretKey_ = self.box_secretkey(keypair_)
        #// @var string $publicKey
        publicKey_ = self.box_publickey(keypair_)
        #// @var string $nonce
        nonce_ = self.generichash(ephemeralPK_ + publicKey_, "", 24)
        #// @var string $keypair
        keypair_ = self.box_keypair_from_secretkey_and_publickey(secretKey_, ephemeralPK_)
        #// @var string $m
        m_ = self.box_open(ciphertext_, nonce_, keypair_)
        try: 
            ParagonIE_Sodium_Compat.memzero(secretKey_)
            ParagonIE_Sodium_Compat.memzero(ephemeralPK_)
            ParagonIE_Sodium_Compat.memzero(nonce_)
        except SodiumException as ex_:
            secretKey_ = None
            ephemeralPK_ = None
            nonce_ = None
        # end try
        return m_
    # end def box_seal_open
    #// 
    #// Used by crypto_box() to get the crypto_secretbox() key.
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $sk
    #// @param string $pk
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def box_beforenm(self, sk_=None, pk_=None):
        
        
        return ParagonIE_Sodium_Core32_HSalsa20.hsalsa20(php_str_repeat(" ", 16), self.scalarmult(sk_, pk_))
    # end def box_beforenm
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @return string
    #// @throws Exception
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def box_keypair(self):
        
        
        sKey_ = random_bytes(32)
        pKey_ = self.scalarmult_base(sKey_)
        return sKey_ + pKey_
    # end def box_keypair
    #// 
    #// @param string $seed
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def box_seed_keypair(self, seed_=None):
        
        
        sKey_ = ParagonIE_Sodium_Core32_Util.substr(hash("sha512", seed_, True), 0, 32)
        pKey_ = self.scalarmult_base(sKey_)
        return sKey_ + pKey_
    # end def box_seed_keypair
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $sKey
    #// @param string $pKey
    #// @return string
    #// @throws TypeError
    #//
    @classmethod
    def box_keypair_from_secretkey_and_publickey(self, sKey_=None, pKey_=None):
        
        
        return ParagonIE_Sodium_Core32_Util.substr(sKey_, 0, 32) + ParagonIE_Sodium_Core32_Util.substr(pKey_, 0, 32)
    # end def box_keypair_from_secretkey_and_publickey
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $keypair
    #// @return string
    #// @throws RangeException
    #// @throws TypeError
    #//
    @classmethod
    def box_secretkey(self, keypair_=None):
        
        
        if ParagonIE_Sodium_Core32_Util.strlen(keypair_) != 64:
            raise php_new_class("RangeException", lambda : RangeException("Must be ParagonIE_Sodium_Compat::CRYPTO_BOX_KEYPAIRBYTES bytes long."))
        # end if
        return ParagonIE_Sodium_Core32_Util.substr(keypair_, 0, 32)
    # end def box_secretkey
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $keypair
    #// @return string
    #// @throws RangeException
    #// @throws TypeError
    #//
    @classmethod
    def box_publickey(self, keypair_=None):
        
        
        if ParagonIE_Sodium_Core32_Util.strlen(keypair_) != ParagonIE_Sodium_Compat.CRYPTO_BOX_KEYPAIRBYTES:
            raise php_new_class("RangeException", lambda : RangeException("Must be ParagonIE_Sodium_Compat::CRYPTO_BOX_KEYPAIRBYTES bytes long."))
        # end if
        return ParagonIE_Sodium_Core32_Util.substr(keypair_, 32, 32)
    # end def box_publickey
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $sKey
    #// @return string
    #// @throws RangeException
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def box_publickey_from_secretkey(self, sKey_=None):
        
        
        if ParagonIE_Sodium_Core32_Util.strlen(sKey_) != ParagonIE_Sodium_Compat.CRYPTO_BOX_SECRETKEYBYTES:
            raise php_new_class("RangeException", lambda : RangeException("Must be ParagonIE_Sodium_Compat::CRYPTO_BOX_SECRETKEYBYTES bytes long."))
        # end if
        return self.scalarmult_base(sKey_)
    # end def box_publickey_from_secretkey
    #// 
    #// Decrypt a message encrypted with box().
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $ciphertext
    #// @param string $nonce
    #// @param string $keypair
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def box_open(self, ciphertext_=None, nonce_=None, keypair_=None):
        
        
        return self.secretbox_open(ciphertext_, nonce_, self.box_beforenm(self.box_secretkey(keypair_), self.box_publickey(keypair_)))
    # end def box_open
    #// 
    #// Calculate a BLAKE2b hash.
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $message
    #// @param string|null $key
    #// @param int $outlen
    #// @return string
    #// @throws RangeException
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def generichash(self, message_=None, key_="", outlen_=32):
        
        
        #// This ensures that ParagonIE_Sodium_Core32_BLAKE2b::$iv is initialized
        ParagonIE_Sodium_Core32_BLAKE2b.pseudoconstructor()
        k_ = None
        if (not php_empty(lambda : key_)):
            #// @var SplFixedArray $k
            k_ = ParagonIE_Sodium_Core32_BLAKE2b.stringtosplfixedarray(key_)
            if k_.count() > ParagonIE_Sodium_Core32_BLAKE2b.KEYBYTES:
                raise php_new_class("RangeException", lambda : RangeException("Invalid key size"))
            # end if
        # end if
        #// @var SplFixedArray $in
        in_ = ParagonIE_Sodium_Core32_BLAKE2b.stringtosplfixedarray(message_)
        #// @var SplFixedArray $ctx
        ctx_ = ParagonIE_Sodium_Core32_BLAKE2b.init(k_, outlen_)
        ParagonIE_Sodium_Core32_BLAKE2b.update(ctx_, in_, in_.count())
        #// @var SplFixedArray $out
        out_ = php_new_class("SplFixedArray", lambda : SplFixedArray(outlen_))
        out_ = ParagonIE_Sodium_Core32_BLAKE2b.finish(ctx_, out_)
        #// @var array<int, int>
        outArray_ = out_.toarray()
        return ParagonIE_Sodium_Core32_Util.intarraytostring(outArray_)
    # end def generichash
    #// 
    #// Finalize a BLAKE2b hashing context, returning the hash.
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $ctx
    #// @param int $outlen
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def generichash_final(self, ctx_=None, outlen_=32):
        
        
        if (not php_is_string(ctx_)):
            raise php_new_class("TypeError", lambda : TypeError("Context must be a string"))
        # end if
        out_ = php_new_class("SplFixedArray", lambda : SplFixedArray(outlen_))
        #// @var SplFixedArray $context
        context_ = ParagonIE_Sodium_Core32_BLAKE2b.stringtocontext(ctx_)
        #// @var SplFixedArray $out
        out_ = ParagonIE_Sodium_Core32_BLAKE2b.finish(context_, out_)
        #// @var array<int, int>
        outArray_ = out_.toarray()
        return ParagonIE_Sodium_Core32_Util.intarraytostring(outArray_)
    # end def generichash_final
    #// 
    #// Initialize a hashing context for BLAKE2b.
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $key
    #// @param int $outputLength
    #// @return string
    #// @throws RangeException
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def generichash_init(self, key_="", outputLength_=32):
        
        
        #// This ensures that ParagonIE_Sodium_Core32_BLAKE2b::$iv is initialized
        ParagonIE_Sodium_Core32_BLAKE2b.pseudoconstructor()
        k_ = None
        if (not php_empty(lambda : key_)):
            k_ = ParagonIE_Sodium_Core32_BLAKE2b.stringtosplfixedarray(key_)
            if k_.count() > ParagonIE_Sodium_Core32_BLAKE2b.KEYBYTES:
                raise php_new_class("RangeException", lambda : RangeException("Invalid key size"))
            # end if
        # end if
        #// @var SplFixedArray $ctx
        ctx_ = ParagonIE_Sodium_Core32_BLAKE2b.init(k_, outputLength_)
        return ParagonIE_Sodium_Core32_BLAKE2b.contexttostring(ctx_)
    # end def generichash_init
    #// 
    #// Initialize a hashing context for BLAKE2b.
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $key
    #// @param int $outputLength
    #// @param string $salt
    #// @param string $personal
    #// @return string
    #// @throws RangeException
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def generichash_init_salt_personal(self, key_="", outputLength_=32, salt_="", personal_=""):
        
        
        #// This ensures that ParagonIE_Sodium_Core32_BLAKE2b::$iv is initialized
        ParagonIE_Sodium_Core32_BLAKE2b.pseudoconstructor()
        k_ = None
        if (not php_empty(lambda : key_)):
            k_ = ParagonIE_Sodium_Core32_BLAKE2b.stringtosplfixedarray(key_)
            if k_.count() > ParagonIE_Sodium_Core32_BLAKE2b.KEYBYTES:
                raise php_new_class("RangeException", lambda : RangeException("Invalid key size"))
            # end if
        # end if
        if (not php_empty(lambda : salt_)):
            s_ = ParagonIE_Sodium_Core32_BLAKE2b.stringtosplfixedarray(salt_)
        else:
            s_ = None
        # end if
        if (not php_empty(lambda : salt_)):
            p_ = ParagonIE_Sodium_Core32_BLAKE2b.stringtosplfixedarray(personal_)
        else:
            p_ = None
        # end if
        #// @var SplFixedArray $ctx
        ctx_ = ParagonIE_Sodium_Core32_BLAKE2b.init(k_, outputLength_, s_, p_)
        return ParagonIE_Sodium_Core32_BLAKE2b.contexttostring(ctx_)
    # end def generichash_init_salt_personal
    #// 
    #// Update a hashing context for BLAKE2b with $message
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $ctx
    #// @param string $message
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def generichash_update(self, ctx_=None, message_=None):
        
        
        #// This ensures that ParagonIE_Sodium_Core32_BLAKE2b::$iv is initialized
        ParagonIE_Sodium_Core32_BLAKE2b.pseudoconstructor()
        #// @var SplFixedArray $context
        context_ = ParagonIE_Sodium_Core32_BLAKE2b.stringtocontext(ctx_)
        #// @var SplFixedArray $in
        in_ = ParagonIE_Sodium_Core32_BLAKE2b.stringtosplfixedarray(message_)
        ParagonIE_Sodium_Core32_BLAKE2b.update(context_, in_, in_.count())
        return ParagonIE_Sodium_Core32_BLAKE2b.contexttostring(context_)
    # end def generichash_update
    #// 
    #// Libsodium's crypto_kx().
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $my_sk
    #// @param string $their_pk
    #// @param string $client_pk
    #// @param string $server_pk
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def keyexchange(self, my_sk_=None, their_pk_=None, client_pk_=None, server_pk_=None):
        
        
        return self.generichash(self.scalarmult(my_sk_, their_pk_) + client_pk_ + server_pk_)
    # end def keyexchange
    #// 
    #// ECDH over Curve25519
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $sKey
    #// @param string $pKey
    #// @return string
    #// 
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def scalarmult(self, sKey_=None, pKey_=None):
        
        
        q_ = ParagonIE_Sodium_Core32_X25519.crypto_scalarmult_curve25519_ref10(sKey_, pKey_)
        self.scalarmult_throw_if_zero(q_)
        return q_
    # end def scalarmult
    #// 
    #// ECDH over Curve25519, using the basepoint.
    #// Used to get a secret key from a public key.
    #// 
    #// @param string $secret
    #// @return string
    #// 
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def scalarmult_base(self, secret_=None):
        
        
        q_ = ParagonIE_Sodium_Core32_X25519.crypto_scalarmult_curve25519_ref10_base(secret_)
        self.scalarmult_throw_if_zero(q_)
        return q_
    # end def scalarmult_base
    #// 
    #// This throws an Error if a zero public key was passed to the function.
    #// 
    #// @param string $q
    #// @return void
    #// @throws SodiumException
    #// @throws TypeError
    #//
    def scalarmult_throw_if_zero(self, q_=None):
        
        
        d_ = 0
        i_ = 0
        while i_ < self.box_curve25519xsalsa20poly1305_SECRETKEYBYTES:
            
            d_ |= ParagonIE_Sodium_Core32_Util.chrtoint(q_[i_])
            i_ += 1
        # end while
        #// branch-free variant of === 0
        if -1 & d_ - 1 >> 8:
            raise php_new_class("SodiumException", lambda : SodiumException("Zero public key is not allowed"))
        # end if
    # end def scalarmult_throw_if_zero
    #// 
    #// XSalsa20-Poly1305 authenticated symmetric-key encryption.
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $plaintext
    #// @param string $nonce
    #// @param string $key
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def secretbox(self, plaintext_=None, nonce_=None, key_=None):
        
        
        #// @var string $subkey
        subkey_ = ParagonIE_Sodium_Core32_HSalsa20.hsalsa20(nonce_, key_)
        #// @var string $block0
        block0_ = php_str_repeat(" ", 32)
        #// @var int $mlen - Length of the plaintext message
        mlen_ = ParagonIE_Sodium_Core32_Util.strlen(plaintext_)
        mlen0_ = mlen_
        if mlen0_ > 64 - self.secretbox_xsalsa20poly1305_ZEROBYTES:
            mlen0_ = 64 - self.secretbox_xsalsa20poly1305_ZEROBYTES
        # end if
        block0_ += ParagonIE_Sodium_Core32_Util.substr(plaintext_, 0, mlen0_)
        #// @var string $block0
        block0_ = ParagonIE_Sodium_Core32_Salsa20.salsa20_xor(block0_, ParagonIE_Sodium_Core32_Util.substr(nonce_, 16, 8), subkey_)
        #// @var string $c
        c_ = ParagonIE_Sodium_Core32_Util.substr(block0_, self.secretbox_xsalsa20poly1305_ZEROBYTES)
        if mlen_ > mlen0_:
            c_ += ParagonIE_Sodium_Core32_Salsa20.salsa20_xor_ic(ParagonIE_Sodium_Core32_Util.substr(plaintext_, self.secretbox_xsalsa20poly1305_ZEROBYTES), ParagonIE_Sodium_Core32_Util.substr(nonce_, 16, 8), 1, subkey_)
        # end if
        state_ = php_new_class("ParagonIE_Sodium_Core32_Poly1305_State", lambda : ParagonIE_Sodium_Core32_Poly1305_State(ParagonIE_Sodium_Core32_Util.substr(block0_, 0, self.onetimeauth_poly1305_KEYBYTES)))
        try: 
            ParagonIE_Sodium_Compat.memzero(block0_)
            ParagonIE_Sodium_Compat.memzero(subkey_)
        except SodiumException as ex_:
            block0_ = None
            subkey_ = None
        # end try
        state_.update(c_)
        #// @var string $c - MAC || ciphertext
        c_ = state_.finish() + c_
        state_ = None
        return c_
    # end def secretbox
    #// 
    #// Decrypt a ciphertext generated via secretbox().
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $ciphertext
    #// @param string $nonce
    #// @param string $key
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def secretbox_open(self, ciphertext_=None, nonce_=None, key_=None):
        
        
        #// @var string $mac
        mac_ = ParagonIE_Sodium_Core32_Util.substr(ciphertext_, 0, self.secretbox_xsalsa20poly1305_MACBYTES)
        #// @var string $c
        c_ = ParagonIE_Sodium_Core32_Util.substr(ciphertext_, self.secretbox_xsalsa20poly1305_MACBYTES)
        #// @var int $clen
        clen_ = ParagonIE_Sodium_Core32_Util.strlen(c_)
        #// @var string $subkey
        subkey_ = ParagonIE_Sodium_Core32_HSalsa20.hsalsa20(nonce_, key_)
        #// @var string $block0
        block0_ = ParagonIE_Sodium_Core32_Salsa20.salsa20(64, ParagonIE_Sodium_Core32_Util.substr(nonce_, 16, 8), subkey_)
        verified_ = ParagonIE_Sodium_Core32_Poly1305.onetimeauth_verify(mac_, c_, ParagonIE_Sodium_Core32_Util.substr(block0_, 0, 32))
        if (not verified_):
            try: 
                ParagonIE_Sodium_Compat.memzero(subkey_)
            except SodiumException as ex_:
                subkey_ = None
            # end try
            raise php_new_class("SodiumException", lambda : SodiumException("Invalid MAC"))
        # end if
        #// @var string $m - Decrypted message
        m_ = ParagonIE_Sodium_Core32_Util.xorstrings(ParagonIE_Sodium_Core32_Util.substr(block0_, self.secretbox_xsalsa20poly1305_ZEROBYTES), ParagonIE_Sodium_Core32_Util.substr(c_, 0, self.secretbox_xsalsa20poly1305_ZEROBYTES))
        if clen_ > self.secretbox_xsalsa20poly1305_ZEROBYTES:
            #// We had more than 1 block, so let's continue to decrypt the rest.
            m_ += ParagonIE_Sodium_Core32_Salsa20.salsa20_xor_ic(ParagonIE_Sodium_Core32_Util.substr(c_, self.secretbox_xsalsa20poly1305_ZEROBYTES), ParagonIE_Sodium_Core32_Util.substr(nonce_, 16, 8), 1, php_str(subkey_))
        # end if
        return m_
    # end def secretbox_open
    #// 
    #// XChaCha20-Poly1305 authenticated symmetric-key encryption.
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $plaintext
    #// @param string $nonce
    #// @param string $key
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def secretbox_xchacha20poly1305(self, plaintext_=None, nonce_=None, key_=None):
        
        
        #// @var string $subkey
        subkey_ = ParagonIE_Sodium_Core32_HChaCha20.hchacha20(ParagonIE_Sodium_Core32_Util.substr(nonce_, 0, 16), key_)
        nonceLast_ = ParagonIE_Sodium_Core32_Util.substr(nonce_, 16, 8)
        #// @var string $block0
        block0_ = php_str_repeat(" ", 32)
        #// @var int $mlen - Length of the plaintext message
        mlen_ = ParagonIE_Sodium_Core32_Util.strlen(plaintext_)
        mlen0_ = mlen_
        if mlen0_ > 64 - self.secretbox_xchacha20poly1305_ZEROBYTES:
            mlen0_ = 64 - self.secretbox_xchacha20poly1305_ZEROBYTES
        # end if
        block0_ += ParagonIE_Sodium_Core32_Util.substr(plaintext_, 0, mlen0_)
        #// @var string $block0
        block0_ = ParagonIE_Sodium_Core32_ChaCha20.streamxoric(block0_, nonceLast_, subkey_)
        #// @var string $c
        c_ = ParagonIE_Sodium_Core32_Util.substr(block0_, self.secretbox_xchacha20poly1305_ZEROBYTES)
        if mlen_ > mlen0_:
            c_ += ParagonIE_Sodium_Core32_ChaCha20.streamxoric(ParagonIE_Sodium_Core32_Util.substr(plaintext_, self.secretbox_xchacha20poly1305_ZEROBYTES), nonceLast_, subkey_, ParagonIE_Sodium_Core32_Util.store64_le(1))
        # end if
        state_ = php_new_class("ParagonIE_Sodium_Core32_Poly1305_State", lambda : ParagonIE_Sodium_Core32_Poly1305_State(ParagonIE_Sodium_Core32_Util.substr(block0_, 0, self.onetimeauth_poly1305_KEYBYTES)))
        try: 
            ParagonIE_Sodium_Compat.memzero(block0_)
            ParagonIE_Sodium_Compat.memzero(subkey_)
        except SodiumException as ex_:
            block0_ = None
            subkey_ = None
        # end try
        state_.update(c_)
        #// @var string $c - MAC || ciphertext
        c_ = state_.finish() + c_
        state_ = None
        return c_
    # end def secretbox_xchacha20poly1305
    #// 
    #// Decrypt a ciphertext generated via secretbox_xchacha20poly1305().
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $ciphertext
    #// @param string $nonce
    #// @param string $key
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def secretbox_xchacha20poly1305_open(self, ciphertext_=None, nonce_=None, key_=None):
        
        
        #// @var string $mac
        mac_ = ParagonIE_Sodium_Core32_Util.substr(ciphertext_, 0, self.secretbox_xchacha20poly1305_MACBYTES)
        #// @var string $c
        c_ = ParagonIE_Sodium_Core32_Util.substr(ciphertext_, self.secretbox_xchacha20poly1305_MACBYTES)
        #// @var int $clen
        clen_ = ParagonIE_Sodium_Core32_Util.strlen(c_)
        #// @var string $subkey
        subkey_ = ParagonIE_Sodium_Core32_HChaCha20.hchacha20(nonce_, key_)
        #// @var string $block0
        block0_ = ParagonIE_Sodium_Core32_ChaCha20.stream(64, ParagonIE_Sodium_Core32_Util.substr(nonce_, 16, 8), subkey_)
        verified_ = ParagonIE_Sodium_Core32_Poly1305.onetimeauth_verify(mac_, c_, ParagonIE_Sodium_Core32_Util.substr(block0_, 0, 32))
        if (not verified_):
            try: 
                ParagonIE_Sodium_Compat.memzero(subkey_)
            except SodiumException as ex_:
                subkey_ = None
            # end try
            raise php_new_class("SodiumException", lambda : SodiumException("Invalid MAC"))
        # end if
        #// @var string $m - Decrypted message
        m_ = ParagonIE_Sodium_Core32_Util.xorstrings(ParagonIE_Sodium_Core32_Util.substr(block0_, self.secretbox_xchacha20poly1305_ZEROBYTES), ParagonIE_Sodium_Core32_Util.substr(c_, 0, self.secretbox_xchacha20poly1305_ZEROBYTES))
        if clen_ > self.secretbox_xchacha20poly1305_ZEROBYTES:
            #// We had more than 1 block, so let's continue to decrypt the rest.
            m_ += ParagonIE_Sodium_Core32_ChaCha20.streamxoric(ParagonIE_Sodium_Core32_Util.substr(c_, self.secretbox_xchacha20poly1305_ZEROBYTES), ParagonIE_Sodium_Core32_Util.substr(nonce_, 16, 8), php_str(subkey_), ParagonIE_Sodium_Core32_Util.store64_le(1))
        # end if
        return m_
    # end def secretbox_xchacha20poly1305_open
    #// 
    #// @param string $key
    #// @return array<int, string> Returns a state and a header.
    #// @throws Exception
    #// @throws SodiumException
    #//
    @classmethod
    def secretstream_xchacha20poly1305_init_push(self, key_=None):
        
        
        #// # randombytes_buf(out, crypto_secretstream_xchacha20poly1305_HEADERBYTES);
        out_ = random_bytes(24)
        #// # crypto_core_hchacha20(state->k, out, k, NULL);
        subkey_ = ParagonIE_Sodium_Core32_HChaCha20.hchacha20(out_, key_)
        state_ = php_new_class("ParagonIE_Sodium_Core32_SecretStream_State", lambda : ParagonIE_Sodium_Core32_SecretStream_State(subkey_, ParagonIE_Sodium_Core32_Util.substr(out_, 16, 8) + php_str_repeat(" ", 4)))
        #// # _crypto_secretstream_xchacha20poly1305_counter_reset(state);
        state_.counterreset()
        #// # memcpy(STATE_INONCE(state), out + crypto_core_hchacha20_INPUTBYTES,
        #// #        crypto_secretstream_xchacha20poly1305_INONCEBYTES);
        #// # memset(state->_pad, 0, sizeof state->_pad);
        return Array(state_.tostring(), out_)
    # end def secretstream_xchacha20poly1305_init_push
    #// 
    #// @param string $key
    #// @param string $header
    #// @return string Returns a state.
    #// @throws Exception
    #//
    @classmethod
    def secretstream_xchacha20poly1305_init_pull(self, key_=None, header_=None):
        
        
        #// # crypto_core_hchacha20(state->k, in, k, NULL);
        subkey_ = ParagonIE_Sodium_Core32_HChaCha20.hchacha20(ParagonIE_Sodium_Core32_Util.substr(header_, 0, 16), key_)
        state_ = php_new_class("ParagonIE_Sodium_Core32_SecretStream_State", lambda : ParagonIE_Sodium_Core32_SecretStream_State(subkey_, ParagonIE_Sodium_Core32_Util.substr(header_, 16)))
        state_.counterreset()
        #// # memcpy(STATE_INONCE(state), in + crypto_core_hchacha20_INPUTBYTES,
        #// #     crypto_secretstream_xchacha20poly1305_INONCEBYTES);
        #// # memset(state->_pad, 0, sizeof state->_pad);
        #// # return 0;
        return state_.tostring()
    # end def secretstream_xchacha20poly1305_init_pull
    #// 
    #// @param string $state
    #// @param string $msg
    #// @param string $aad
    #// @param int $tag
    #// @return string
    #// @throws SodiumException
    #//
    @classmethod
    def secretstream_xchacha20poly1305_push(self, state_=None, msg_=None, aad_="", tag_=0):
        
        
        st_ = ParagonIE_Sodium_Core32_SecretStream_State.fromstring(state_)
        #// # crypto_onetimeauth_poly1305_state poly1305_state;
        #// # unsigned char                     block[64U];
        #// # unsigned char                     slen[8U];
        #// # unsigned char                    *c;
        #// # unsigned char                    *mac;
        msglen_ = ParagonIE_Sodium_Core32_Util.strlen(msg_)
        aadlen_ = ParagonIE_Sodium_Core32_Util.strlen(aad_)
        if msglen_ + 63 >> 6 > 4294967294:
            raise php_new_class("SodiumException", lambda : SodiumException("message cannot be larger than SODIUM_CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_MESSAGEBYTES_MAX bytes"))
        # end if
        #// # if (outlen_p != NULL) {
        #// #     *outlen_p = 0U;
        #// # }
        #// # if (mlen > crypto_secretstream_xchacha20poly1305_MESSAGEBYTES_MAX) {
        #// #     sodium_misuse();
        #// # }
        #// # crypto_stream_chacha20_ietf(block, sizeof block, state->nonce, state->k);
        #// # crypto_onetimeauth_poly1305_init(&poly1305_state, block);
        #// # sodium_memzero(block, sizeof block);
        auth_ = php_new_class("ParagonIE_Sodium_Core32_Poly1305_State", lambda : ParagonIE_Sodium_Core32_Poly1305_State(ParagonIE_Sodium_Core32_ChaCha20.ietfstream(32, st_.getcombinednonce(), st_.getkey())))
        #// # crypto_onetimeauth_poly1305_update(&poly1305_state, ad, adlen);
        auth_.update(aad_)
        #// # crypto_onetimeauth_poly1305_update(&poly1305_state, _pad0,
        #// #     (0x10 - adlen) & 0xf);
        auth_.update(php_str_repeat(" ", 16 - aadlen_ & 15))
        #// # memset(block, 0, sizeof block);
        #// # block[0] = tag;
        #// # crypto_stream_chacha20_ietf_xor_ic(block, block, sizeof block,
        #// #                                    state->nonce, 1U, state->k);
        block_ = ParagonIE_Sodium_Core32_ChaCha20.ietfstreamxoric(ParagonIE_Sodium_Core32_Util.inttochr(tag_) + php_str_repeat(" ", 63), st_.getcombinednonce(), st_.getkey(), ParagonIE_Sodium_Core32_Util.store64_le(1))
        #// # crypto_onetimeauth_poly1305_update(&poly1305_state, block, sizeof block);
        auth_.update(block_)
        #// # out[0] = block[0];
        out_ = block_[0]
        #// # c = out + (sizeof tag);
        #// # crypto_stream_chacha20_ietf_xor_ic(c, m, mlen, state->nonce, 2U, state->k);
        cipher_ = ParagonIE_Sodium_Core32_ChaCha20.ietfstreamxoric(msg_, st_.getcombinednonce(), st_.getkey(), ParagonIE_Sodium_Core32_Util.store64_le(2))
        #// # crypto_onetimeauth_poly1305_update(&poly1305_state, c, mlen);
        auth_.update(cipher_)
        out_ += cipher_
        cipher_ = None
        #// # crypto_onetimeauth_poly1305_update
        #// # (&poly1305_state, _pad0, (0x10 - (sizeof block) + mlen) & 0xf);
        auth_.update(php_str_repeat(" ", 16 - 64 + msglen_ & 15))
        #// # STORE64_LE(slen, (uint64_t) adlen);
        slen_ = ParagonIE_Sodium_Core32_Util.store64_le(aadlen_)
        #// # crypto_onetimeauth_poly1305_update(&poly1305_state, slen, sizeof slen);
        auth_.update(slen_)
        #// # STORE64_LE(slen, (sizeof block) + mlen);
        slen_ = ParagonIE_Sodium_Core32_Util.store64_le(64 + msglen_)
        #// # crypto_onetimeauth_poly1305_update(&poly1305_state, slen, sizeof slen);
        auth_.update(slen_)
        #// # mac = c + mlen;
        #// # crypto_onetimeauth_poly1305_final(&poly1305_state, mac);
        mac_ = auth_.finish()
        out_ += mac_
        auth_ = None
        #// # XOR_BUF(STATE_INONCE(state), mac,
        #// #     crypto_secretstream_xchacha20poly1305_INONCEBYTES);
        st_.xornonce(mac_)
        #// # sodium_increment(STATE_COUNTER(state),
        #// #     crypto_secretstream_xchacha20poly1305_COUNTERBYTES);
        st_.incrementcounter()
        #// Overwrite by reference:
        state_ = st_.tostring()
        #// @var bool $rekey
        rekey_ = tag_ & ParagonIE_Sodium_Compat.CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_REKEY != 0
        #// # if ((tag & crypto_secretstream_xchacha20poly1305_TAG_REKEY) != 0 ||
        #// #     sodium_is_zero(STATE_COUNTER(state),
        #// #         crypto_secretstream_xchacha20poly1305_COUNTERBYTES)) {
        #// #     crypto_secretstream_xchacha20poly1305_rekey(state);
        #// # }
        if rekey_ or st_.needsrekey():
            #// DO REKEY
            self.secretstream_xchacha20poly1305_rekey(state_)
        # end if
        #// # if (outlen_p != NULL) {
        #// #     *outlen_p = crypto_secretstream_xchacha20poly1305_ABYTES + mlen;
        #// # }
        return out_
    # end def secretstream_xchacha20poly1305_push
    #// 
    #// @param string $state
    #// @param string $cipher
    #// @param string $aad
    #// @return bool|array{0: string, 1: int}
    #// @throws SodiumException
    #//
    @classmethod
    def secretstream_xchacha20poly1305_pull(self, state_=None, cipher_=None, aad_=""):
        
        
        st_ = ParagonIE_Sodium_Core32_SecretStream_State.fromstring(state_)
        cipherlen_ = ParagonIE_Sodium_Core32_Util.strlen(cipher_)
        #// #     mlen = inlen - crypto_secretstream_xchacha20poly1305_ABYTES;
        msglen_ = cipherlen_ - ParagonIE_Sodium_Compat.CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_ABYTES
        aadlen_ = ParagonIE_Sodium_Core32_Util.strlen(aad_)
        #// #     if (mlen > crypto_secretstream_xchacha20poly1305_MESSAGEBYTES_MAX) {
        #// #         sodium_misuse();
        #// #     }
        if msglen_ + 63 >> 6 > 4294967294:
            raise php_new_class("SodiumException", lambda : SodiumException("message cannot be larger than SODIUM_CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_MESSAGEBYTES_MAX bytes"))
        # end if
        #// #     crypto_stream_chacha20_ietf(block, sizeof block, state->nonce, state->k);
        #// #     crypto_onetimeauth_poly1305_init(&poly1305_state, block);
        #// #     sodium_memzero(block, sizeof block);
        auth_ = php_new_class("ParagonIE_Sodium_Core32_Poly1305_State", lambda : ParagonIE_Sodium_Core32_Poly1305_State(ParagonIE_Sodium_Core32_ChaCha20.ietfstream(32, st_.getcombinednonce(), st_.getkey())))
        #// #     crypto_onetimeauth_poly1305_update(&poly1305_state, ad, adlen);
        auth_.update(aad_)
        #// #     crypto_onetimeauth_poly1305_update(&poly1305_state, _pad0,
        #// #         (0x10 - adlen) & 0xf);
        auth_.update(php_str_repeat(" ", 16 - aadlen_ & 15))
        #// #     memset(block, 0, sizeof block);
        #// #     block[0] = in[0];
        #// #     crypto_stream_chacha20_ietf_xor_ic(block, block, sizeof block,
        #// #                                        state->nonce, 1U, state->k);
        block_ = ParagonIE_Sodium_Core32_ChaCha20.ietfstreamxoric(cipher_[0] + php_str_repeat(" ", 63), st_.getcombinednonce(), st_.getkey(), ParagonIE_Sodium_Core32_Util.store64_le(1))
        #// #     tag = block[0];
        #// #     block[0] = in[0];
        #// #     crypto_onetimeauth_poly1305_update(&poly1305_state, block, sizeof block);
        tag_ = ParagonIE_Sodium_Core32_Util.chrtoint(block_[0])
        block_[0] = cipher_[0]
        auth_.update(block_)
        #// #     c = in + (sizeof tag);
        #// #     crypto_onetimeauth_poly1305_update(&poly1305_state, c, mlen);
        auth_.update(ParagonIE_Sodium_Core32_Util.substr(cipher_, 1, msglen_))
        #// #     crypto_onetimeauth_poly1305_update
        #// #     (&poly1305_state, _pad0, (0x10 - (sizeof block) + mlen) & 0xf);
        auth_.update(php_str_repeat(" ", 16 - 64 + msglen_ & 15))
        #// #     STORE64_LE(slen, (uint64_t) adlen);
        #// #     crypto_onetimeauth_poly1305_update(&poly1305_state, slen, sizeof slen);
        slen_ = ParagonIE_Sodium_Core32_Util.store64_le(aadlen_)
        auth_.update(slen_)
        #// #     STORE64_LE(slen, (sizeof block) + mlen);
        #// #     crypto_onetimeauth_poly1305_update(&poly1305_state, slen, sizeof slen);
        slen_ = ParagonIE_Sodium_Core32_Util.store64_le(64 + msglen_)
        auth_.update(slen_)
        #// #     crypto_onetimeauth_poly1305_final(&poly1305_state, mac);
        #// #     sodium_memzero(&poly1305_state, sizeof poly1305_state);
        mac_ = auth_.finish()
        #// #     stored_mac = c + mlen;
        #// #     if (sodium_memcmp(mac, stored_mac, sizeof mac) != 0) {
        #// #     sodium_memzero(mac, sizeof mac);
        #// #         return -1;
        #// #     }
        stored_ = ParagonIE_Sodium_Core32_Util.substr(cipher_, msglen_ + 1, 16)
        if (not ParagonIE_Sodium_Core32_Util.hashequals(mac_, stored_)):
            return False
        # end if
        #// #     crypto_stream_chacha20_ietf_xor_ic(m, c, mlen, state->nonce, 2U, state->k);
        out_ = ParagonIE_Sodium_Core32_ChaCha20.ietfstreamxoric(ParagonIE_Sodium_Core32_Util.substr(cipher_, 1, msglen_), st_.getcombinednonce(), st_.getkey(), ParagonIE_Sodium_Core32_Util.store64_le(2))
        #// #     XOR_BUF(STATE_INONCE(state), mac,
        #// #         crypto_secretstream_xchacha20poly1305_INONCEBYTES);
        st_.xornonce(mac_)
        #// #     sodium_increment(STATE_COUNTER(state),
        #// #         crypto_secretstream_xchacha20poly1305_COUNTERBYTES);
        st_.incrementcounter()
        #// #     if ((tag & crypto_secretstream_xchacha20poly1305_TAG_REKEY) != 0 ||
        #// #         sodium_is_zero(STATE_COUNTER(state),
        #// #             crypto_secretstream_xchacha20poly1305_COUNTERBYTES)) {
        #// #         crypto_secretstream_xchacha20poly1305_rekey(state);
        #// #     }
        #// Overwrite by reference:
        state_ = st_.tostring()
        #// @var bool $rekey
        rekey_ = tag_ & ParagonIE_Sodium_Compat.CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_REKEY != 0
        if rekey_ or st_.needsrekey():
            #// DO REKEY
            self.secretstream_xchacha20poly1305_rekey(state_)
        # end if
        return Array(out_, tag_)
    # end def secretstream_xchacha20poly1305_pull
    #// 
    #// @param string $state
    #// @return void
    #// @throws SodiumException
    #//
    @classmethod
    def secretstream_xchacha20poly1305_rekey(self, state_=None):
        
        
        st_ = ParagonIE_Sodium_Core32_SecretStream_State.fromstring(state_)
        #// # unsigned char new_key_and_inonce[crypto_stream_chacha20_ietf_KEYBYTES +
        #// # crypto_secretstream_xchacha20poly1305_INONCEBYTES];
        #// # size_t        i;
        #// # for (i = 0U; i < crypto_stream_chacha20_ietf_KEYBYTES; i++) {
        #// #     new_key_and_inonce[i] = state->k[i];
        #// # }
        new_key_and_inonce_ = st_.getkey()
        #// # for (i = 0U; i < crypto_secretstream_xchacha20poly1305_INONCEBYTES; i++) {
        #// #     new_key_and_inonce[crypto_stream_chacha20_ietf_KEYBYTES + i] =
        #// #         STATE_INONCE(state)[i];
        #// # }
        new_key_and_inonce_ += ParagonIE_Sodium_Core32_Util.substr(st_.getnonce(), 0, 8)
        #// # crypto_stream_chacha20_ietf_xor(new_key_and_inonce, new_key_and_inonce,
        #// #                                 sizeof new_key_and_inonce,
        #// #                                 state->nonce, state->k);
        st_.rekey(ParagonIE_Sodium_Core32_ChaCha20.ietfstreamxoric(new_key_and_inonce_, st_.getcombinednonce(), st_.getkey(), ParagonIE_Sodium_Core32_Util.store64_le(0)))
        #// # for (i = 0U; i < crypto_stream_chacha20_ietf_KEYBYTES; i++) {
        #// #     state->k[i] = new_key_and_inonce[i];
        #// # }
        #// # for (i = 0U; i < crypto_secretstream_xchacha20poly1305_INONCEBYTES; i++) {
        #// #     STATE_INONCE(state)[i] =
        #// #          new_key_and_inonce[crypto_stream_chacha20_ietf_KEYBYTES + i];
        #// # }
        #// # _crypto_secretstream_xchacha20poly1305_counter_reset(state);
        st_.counterreset()
        state_ = st_.tostring()
    # end def secretstream_xchacha20poly1305_rekey
    #// 
    #// Detached Ed25519 signature.
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $message
    #// @param string $sk
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def sign_detached(self, message_=None, sk_=None):
        
        
        return ParagonIE_Sodium_Core32_Ed25519.sign_detached(message_, sk_)
    # end def sign_detached
    #// 
    #// Attached Ed25519 signature. (Returns a signed message.)
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $message
    #// @param string $sk
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def sign(self, message_=None, sk_=None):
        
        
        return ParagonIE_Sodium_Core32_Ed25519.sign(message_, sk_)
    # end def sign
    #// 
    #// Opens a signed message. If valid, returns the message.
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $signedMessage
    #// @param string $pk
    #// @return string
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def sign_open(self, signedMessage_=None, pk_=None):
        
        
        return ParagonIE_Sodium_Core32_Ed25519.sign_open(signedMessage_, pk_)
    # end def sign_open
    #// 
    #// Verify a detached signature of a given message and public key.
    #// 
    #// @internal Do not use this directly. Use ParagonIE_Sodium_Compat.
    #// 
    #// @param string $signature
    #// @param string $message
    #// @param string $pk
    #// @return bool
    #// @throws SodiumException
    #// @throws TypeError
    #//
    @classmethod
    def sign_verify_detached(self, signature_=None, message_=None, pk_=None):
        
        
        return ParagonIE_Sodium_Core32_Ed25519.verify_detached(signature_, message_, pk_)
    # end def sign_verify_detached
# end class ParagonIE_Sodium_Crypto32

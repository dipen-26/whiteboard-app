# 🔐 AUTH & USER MANAGEMENT VERIFICATION SCRIPT

## 🎯 OBJECTIVE:
Check if all user management and JWT authentication features are implemented correctly in this Django project.

---

## 1. ✅ CUSTOM USER MODEL

- [ ] Is there a model like `CustomUser(AbstractUser)` in `users/models.py`?
- [ ] Does it have a `role` field with choices: `owner`, `editor`, `viewer`?
- [ ] Is `AUTH_USER_MODEL = 'users.CustomUser'` set in `settings.py`?

---

## 2. ✅ JWT AUTHENTICATION

- [ ] Is `rest_framework_simplejwt` installed and configured?
- [ ] Are these endpoints present in `urls.py`?
  - `/api/token/`
  - `/api/token/refresh/`
- [ ] Is `JWTAuthentication` listed in `DEFAULT_AUTHENTICATION_CLASSES`?

---

## 3. ✅ USER REGISTRATION

- [ ] Is there a `RegisterSerializer` in `users/serializers.py`?
- [ ] Does it accept `username`, `email`, `password`, and `role`?
- [ ] Does the `RegisterView` exist in `users/views.py`?
- [ ] Is it routed in `users/urls.py` as `/api/users/register/`?

---

## 4. ✅ AUTHENTICATED ACCESS

- [ ] Is there a view that uses `permission_classes = [IsAuthenticated]`?
- [ ] Example: `/api/users/secure/` or similar test endpoint

---

## 5. ✅ ROLE-BASED PERMISSIONS

- [ ] Is there a `permissions.py` with these classes?
  - `IsOwner`
  - `IsEditor`
  - `IsViewer`
- [ ] Are views using them correctly like:
  - `permission_classes = [IsOwner]`
  - `permission_classes = [IsEditor] | [IsOwner]`

---

## 6. ✅ USERS/URLS

- [ ] Are the following routes defined in `users/urls.py`?
  - `/register/`
  - `/secure/`
  - `/owner/`
  - `/editor/`
  - `/viewer/`

---

## 7. ✅ ADMIN PANEL (OPTIONAL)

- [ ] Can roles be edited from Django admin (`admin.py` registered)?
- [ ] Is `CustomUser` visible in Django admin?

---

## 8. ✅ TESTING INTEGRATION

- [ ] Do authenticated requests work with Bearer tokens?
- [ ] Do unauthorized requests return 401?
- [ ] Does each role see the expected message in `/owner/`, `/editor/`, `/viewer/`?

---

## ✅ RESULT

If all boxes are checked, the authentication and user role system is fully functional.

🎉 Proceed to building whiteboard features!

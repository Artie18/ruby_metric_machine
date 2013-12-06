def for_set_permissions
    temp =[]
    permissions = Abt::AccessControl.permissions
    permissions = Abt::AccessControl.user_permissions      if self.builtin == BUILTIN_USER
    permissions = Abt::AccessControl.manager_permissions   if self.builtin == BUILTIN_MANAGER
    permissions = Abt::AccessControl.architect_permissions if self.builtin == BUILTIN_ARCHITECT
    permissions = Abt::AccessControl.designer_permissions  if self.builtin == BUILTIN_DESIGNER
    permissions = Abt::AccessControl.customer_permissions  if self.builtin == BUILTIN_CUSTOMER
    permissions = Abt::AccessControl.vendor_permissions    if self.builtin == BUILTIN_VENDOR
    permissions = Abt::AccessControl.dealer_permissions    if self.builtin == BUILTIN_DEALER
    permissions - Abt::AccessControl.public_permissions
  end
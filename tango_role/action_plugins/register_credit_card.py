from ansible.plugins.action import ActionBase
import sys
sys.path.append("")
from tango_role.tango import Tango


class ActionModule(ActionBase, Tango):
    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)
        module_args = self._task.args.copy()

        t = Tango()
        return t.register_credit_card(
            customer_id = module_args.get("customer_id", "default"),
            account = module_args.get("account", "default"),
            label = module_args.get("label", "default"),
            ip_address = module_args.get("ip_address", "default"),
            card_number = module_args.get("card_number", "default"),
            card_expiration = module_args.get("card_expiration", "default"),
            card_verification_number = module_args.get("card_verification_number", "default"),
            billing_first_name = module_args.get("billing_first_name", "default"),
            billing_last_name = module_args.get("billing_last_name", "default"),
            billing_address_line1 = module_args.get("billing_address_line1", "default"),
            billing_city = module_args.get("billing_city", "default"),
            billing_state = module_args.get("billing_state", "default"),
            billing_postal = module_args.get("billing_postal", "default"),
            billing_country = module_args.get("billing_country", "default"),
            billing_email = module_args.get("billing_email", "default"),
            contact_full_name = module_args.get("contact_full_name", "default"),
            contact_email = module_args.get("contact_email", "default")
        )
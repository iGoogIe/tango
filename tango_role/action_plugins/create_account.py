from ansible.plugins.action import ActionBase
import sys
sys.path.append("")
from tango_role.tango import Tango


class ActionModule(ActionBase, Tango):
    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)
        module_args = self._task.args.copy()

        t = Tango()
        return t.create_account(
            customer_id = module_args.get("customer_id", "default"),
            account = module_args.get("account", "default"),
            email = module_args.get("email", "default")
        )
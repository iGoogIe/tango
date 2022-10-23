from ansible.plugins.action import ActionBase
import sys
sys.path.append("")
from tango import Tango


class ActionModule(ActionBase, Tango):
    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)
        module_args = self._task.args.copy()

        t = Tango()
        return t.create_customer(
            customer_id = module_args.get("customer_id", "default"),
            display_name = module_args.get("display_name", "default")
        )
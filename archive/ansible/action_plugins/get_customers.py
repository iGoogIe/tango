from ansible.plugins.action import ActionBase
import sys
sys.path.append("")
from tango import Tango


class ActionModule(ActionBase, Tango):
    def run(self, tmp=None, task_vars=None):
        
        # set to result and then return in the Tango Method
        result = super(ActionModule, self).run(tmp, task_vars)

        module_args = self._task.args.copy()

        ## Example to use another module i.e setup
        # module_return = self._execute_module(
        #     module_name='setup',
        #     module_args=module_args,
        #     task_vars=task_vars, 
        #     tmp=tmp
        # )

        t = Tango()
        return t.get_customers()


        ##Example Response Below
        # return dict(ansible_facts=dict({"result" : t_response}))

        #### Example provided in docs. 
        # ret = dict()
        # remote_date = None
        # if not module_return.get('failed'):
        #     for key, value in module_return['ansible_facts'].items():
        #         if key == 'ansible_date_time':
        #             remote_date = value['iso8601']

        # if remote_date:
        #     remote_date_obj = datetime.strptime(remote_date, '%Y-%m-%dT%H:%M:%SZ')
        #     time_delta = datetime.utcnow() - remote_date_obj
        #     ret['delta_seconds'] = time_delta.seconds
        #     ret['delta_days'] = time_delta.days
        #     ret['delta_microseconds'] = time_delta.microseconds

        # return dict(ansible_facts=dict(ret))
        ####
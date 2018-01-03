from phue import Bridge


class MultiBridge(Bridge):

    def send_multi(self, step):
        if 'transitiontime' in step:
            step.pop('transitiontime', step['transitiontime'])
        print(self.request('PUT', '/api/' + self.username + '/config', step))

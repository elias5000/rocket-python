from rocketchat.calls.base import PostMixin, RocketChatBase


class SendMessage(PostMixin, RocketChatBase):
    endpoint = '/api/v1/chat.sendMessage'

    def build_endpoint(self, **kwargs):
        return self.endpoint

    def build_payload(self, **kwargs):
        payload = {
            'message': {
                'msg': kwargs.get('message'),
                'rid': kwargs.get('room_id'),
            }
        }

        if kwargs.get('thread_message_id'):
            payload['message']['tmid'] = kwargs.get('thread_message_id')

        return payload

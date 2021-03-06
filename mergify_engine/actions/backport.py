# -*- encoding: utf-8 -*-
#
#  Copyright © 2018 Mehdi Abaakouk <sileht@sileht.net>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from mergify_engine.actions import copy


class BackportAction(copy.CopyAction):
    is_command = True

    KIND = "backport"
    SUCCESS_MESSAGE = "Backports have been created"

    @staticmethod
    def command_to_config(string):
        return {"branches": string.split(" ")}

    def run(
        self,
        installation_id,
        installation_token,
        event_type,
        data,
        pull,
        missing_conditions,
    ):
        if not pull.g_pull.merged:
            return None, "Waiting for the pull request to get merged", ""
        return super().run(
            installation_id,
            installation_token,
            event_type,
            data,
            pull,
            missing_conditions,
        )

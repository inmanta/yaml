"""
    Copyright 2022 Inmanta

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Contact: code@inmanta.com
"""

import os
import shutil


def test_network_inventory(project):
    files_in_project = os.path.join(project._test_project_dir, "files")
    os.makedirs(files_in_project)
    base_path = os.path.join(
        os.path.dirname(__file__), "../examples/network_inventory/"
    )

    shutil.copy(
        os.path.join(base_path, "inventory.yaml"),
        os.path.join(files_in_project, "inventory.yaml"),
    )

    with open(
        os.path.join(
            os.path.dirname(__file__), "../examples/network_inventory/inventory.cf"
        ),
        "r",
    ) as fh:
        project.compile(fh.read())

    for line in [
        "Router test1: 10.0.0.1",
        "Router test2: 10.0.0.2",
        "Interface test1.eth0: 192.168.2.1/24",
        "Interface test1.eth1: 192.168.3.1/24",
        "Interface test2.eth0: 192.168.4.1/24",
        "Interface test2.eth1: 192.168.5.1/24",
    ]:
        assert line in project.get_stdout()

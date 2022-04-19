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
import yaml
from pytest_inmanta.plugin import Project


def test_basics(project: Project) -> None:
    test_content = {"a": ["a", "b", "c"]}
    yaml_content = yaml.safe_dump(test_content)
    project.add_mock_file("files", "test.yaml", yaml_content)
    project.compile(
        f"""
            import yaml
            import unittest

            a = yaml::load("unittest/test.yaml")
            b = yaml::loads(\"""{yaml_content}\""")

            entity Out:
                dict a
                dict b
            end

            Out(a=a, b=b)

            implement Out using std::none
        """
    )

    instance = project.get_instances("__config__::Out")[0]
    assert instance.a == test_content
    assert instance.b == test_content


def test_readme(project):

    project.compile(
        """
    import yaml
    yaml_dict_c = yaml::loads(\"""key: value\""")
    yaml_dict_c = {"key":"value"}
    """
    )

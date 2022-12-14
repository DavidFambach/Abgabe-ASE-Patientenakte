import json

from app_file.models import StorageUser, File, Directory, Share
from app_file.serializers import serialize_user_info, serialize_storage_user, serialize_file, serialize_directory, serialize_share
from django.test import TestCase
from typing import Any, Union

UNORDERED_LISTS_USER_INFO = [
    ("ownShares",),
    ("receivedShares",)
]
UNORDERED_LISTS_DIRECTORY_WITH_CHILDREN = [
    ("children",),
]
SERIALIZED_USER_INFO_1 = json.loads("""
{
    "personalRootDirectory": 1,
    "contacts": [
        {
            "id": 2,
            "displayName": "Testarzt"
        }
    ],
    "ownShares": [
        {
            "id": 1,
            "issuer": {
                "id": 1,
                "displayName": "Testpatient"
            },
            "subject": {
                "id": 2,
                "displayName": "Testarzt"
            },
            "target": {
                "type": "directory",
                "id": 3
            },
            "canWrite": false
        },
        {
            "id": 2,
            "issuer": {
                "id": 1,
                "displayName": "Testpatient"
            },
            "subject": {
                "id": 2,
                "displayName": "Testarzt"
            },
            "target": {
                "type": "file",
                "id": 4
            },
            "canWrite": true
        }
    ],
    "receivedShares": []
}""")
SERIALIZED_USER_INFO_2 = json.loads("""
{
    "personalRootDirectory": 5,
    "contacts": [],
    "ownShares": [],
    "receivedShares": [
        {
            "id": 2,
            "issuer": {
                "id": 1,
                "displayName": "Testpatient"
            },
            "subject": {
                "id": 2,
                "displayName": "Testarzt"
            },
            "target": {
                "type": "file",
                "id": 4
            },
            "canWrite": true
        },
        {
            "id": 1,
            "issuer": {
                "id": 1,
                "displayName": "Testpatient"
            },
            "subject": {
                "id": 2,
                "displayName": "Testarzt"
            },
            "target": {
                "type": "directory",
                "id": 3
            },
            "canWrite": false
        }
    ]
}""")

SERIALIZED_USER_1 = json.loads("""
{
    "id": 1,
    "displayName": "Testpatient"
}""")
SERIALIZED_USER_2 = json.loads("""
{
    "id": 2,
    "displayName": "Testarzt"
}""")

SERIALIZED_FILE_1 = json.loads("""
{
    "id": 1,
    "name": "Beispieldatei",
    "owner": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "parentDirectory": 1
}""")
SERIALIZED_FILE_2 = json.loads("""
{
    "id": 2,
    "name": "Zweite Beispieldatei",
    "owner": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "parentDirectory": 1
}""")
SERIALIZED_FILE_3 = json.loads("""
{
    "id": 3,
    "name": "Durch Elternverzeichnis freigegebene Datei",
    "owner": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "parentDirectory": 3
}""")
SERIALIZED_FILE_4 = json.loads("""
{
    "id": 4,
    "name": "Direkt freigegebene Datei",
    "owner": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "parentDirectory": 2
}""")

SERIALIZED_DIRECTORY_1 = json.loads("""
{
    "id": 1,
    "name": "Testpatient Wurzelverzeichnis",
    "owner": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "parentDirectory": null
}""")
SERIALIZED_DIRECTORY_1_WITH_CHILDREN = json.loads("""
{
    "id": 1,
    "name": "Testpatient Wurzelverzeichnis",
    "owner": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "children": [
        {
            "type": "directory",
            "directory": {
                "id": 2,
                "name": "Unterverzeichnis",
                "owner": {
                    "id": 1,
                    "displayName": "Testpatient"
                },
                "parentDirectory": 1
            }
        },
        {
            "type": "directory",
            "directory": {
                "id": 3,
                "name": "Freigegebenes Unterverzeichnis",
                "owner": {
                    "id": 1,
                    "displayName": "Testpatient"
                },
                "parentDirectory": 1
            }
        },
        {
            "type": "file",
            "file": {
                "id": 1,
                "name": "Beispieldatei",
                "owner": {
                    "id": 1,
                    "displayName": "Testpatient"
                },
                "parentDirectory": 1
            }
        },
        {
            "type": "file",
            "file": {
                "id": 2,
                "name": "Zweite Beispieldatei",
                "owner": {
                    "id": 1,
                    "displayName": "Testpatient"
                },
                "parentDirectory": 1
            }
        }
    ],
    "parentDirectory": null
}""")
SERIALIZED_DIRECTORY_2 = json.loads("""
{
    "id": 2,
    "name": "Unterverzeichnis",
    "owner": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "parentDirectory": 1
}""")
SERIALIZED_DIRECTORY_2_WITH_CHILDREN = json.loads("""
{
    "id": 2,
    "name": "Unterverzeichnis",
    "owner": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "children": [
        {
            "type": "directory",
            "directory": {
                "id": 4,
                "name": "Unterunterverzeichnis",
                "owner": {
                    "id": 1,
                    "displayName": "Testpatient"
                },
                "parentDirectory": 2
            }
        },
        {
            "type": "file",
            "file": {
                "id": 4,
                "name": "Direkt freigegebene Datei",
                "owner": {
                    "id": 1,
                    "displayName": "Testpatient"
                },
                "parentDirectory": 2
            }
        }
    ],
    "parentDirectory": 1
}""")
SERIALIZED_DIRECTORY_3 = json.loads("""
{
    "id": 3,
    "name": "Freigegebenes Unterverzeichnis",
    "owner": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "parentDirectory": 1
}""")
SERIALIZED_DIRECTORY_3_WITH_CHILDREN = json.loads("""
{
    "id": 3,
    "name": "Freigegebenes Unterverzeichnis",
    "owner": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "children": [
        {
            "type": "file",
            "file": {
                "id": 3,
                "name": "Durch Elternverzeichnis freigegebene Datei",
                "owner": {
                    "id": 1,
                    "displayName": "Testpatient"
                },
                "parentDirectory": 3
            }
        }
    ],
    "parentDirectory": 1
}""")
SERIALIZED_DIRECTORY_4 = json.loads("""
{
    "id": 4,
    "name": "Unterunterverzeichnis",
    "owner": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "parentDirectory": 2
}""")
SERIALIZED_DIRECTORY_4_WITH_CHILDREN = json.loads("""
{
    "id": 4,
    "name": "Unterunterverzeichnis",
    "owner": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "children": [],
    "parentDirectory": 2
}""")
SERIALIZED_DIRECTORY_5 = json.loads("""
{
    "id": 5,
    "name": "Testarzt Wurzelverzeichnis",
    "owner": {
        "id": 2,
        "displayName": "Testarzt"
    },
    "parentDirectory": null
}""")
SERIALIZED_DIRECTORY_5_WITH_CHILDREN = json.loads("""
{
    "id": 5,
    "name": "Testarzt Wurzelverzeichnis",
    "owner": {
        "id": 2,
        "displayName": "Testarzt"
    },
    "children": [],
    "parentDirectory": null
}""")

SERIALIZED_SHARE_1 = json.loads("""
{
    "id": 1,
    "issuer": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "subject": {
        "id": 2,
        "displayName": "Testarzt"
    },
    "target": {
        "type": "directory",
        "id": 3
    },
    "canWrite": false
}""")
SERIALIZED_SHARE_1_WITH_TARGET = json.loads("""
{
    "id": 1,
    "issuer": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "subject": {
        "id": 2,
        "displayName": "Testarzt"
    },
    "target": {
        "type": "directory",
        "id": 3,
        "directory": {
            "id": 3,
            "name": "Freigegebenes Unterverzeichnis",
            "owner": {
                "id": 1,
                "displayName": "Testpatient"
            },
            "parentDirectory": 1
        }
    },
    "canWrite": false
}""")
SERIALIZED_SHARE_2 = json.loads("""
{
    "id": 2,
    "issuer": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "subject": {
        "id": 2,
        "displayName": "Testarzt"
    },
    "target": {
        "type": "file",
        "id": 4
    },
    "canWrite": true
}""")
SERIALIZED_SHARE_2_WITH_TARGET = json.loads("""
{
    "id": 2,
    "issuer": {
        "id": 1,
        "displayName": "Testpatient"
    },
    "subject": {
        "id": 2,
        "displayName": "Testarzt"
    },
    "target": {
        "type": "file",
        "id": 4,
        "file": {
            "id": 4,
            "name": "Direkt freigegebene Datei",
            "owner": {
                "id": 1,
                "displayName": "Testpatient"
            },
            "parentDirectory": 2
        }
    },
    "canWrite": true
}""")

class TestSerializers(TestCase):

    fixtures = ["test_files"]
    maxDiff = None

    def test_serialize_user_info(self):
        self.assert_equal_with_unordered_distinct_lists(UNORDERED_LISTS_USER_INFO, SERIALIZED_USER_INFO_1, serialize_user_info(StorageUser.objects.get(id=1)))
        self.assert_equal_with_unordered_distinct_lists(UNORDERED_LISTS_USER_INFO, SERIALIZED_USER_INFO_2, serialize_user_info(StorageUser.objects.get(id=2)))

    def test_serialize_user(self):
        self.assertEqual(SERIALIZED_USER_1, serialize_storage_user(StorageUser.objects.get(id=1)))
        self.assertEqual(SERIALIZED_USER_2, serialize_storage_user(StorageUser.objects.get(id=2)))

    def test_serialize_file(self):
        self.assertEqual(SERIALIZED_FILE_1, serialize_file(File.objects.get(id=1)))
        self.assertEqual(SERIALIZED_FILE_2, serialize_file(File.objects.get(id=2)))
        self.assertEqual(SERIALIZED_FILE_3, serialize_file(File.objects.get(id=3)))
        self.assertEqual(SERIALIZED_FILE_4, serialize_file(File.objects.get(id=4)))

    def test_serialize_directory(self):
        self.assert_equal_with_unordered_distinct_lists(UNORDERED_LISTS_DIRECTORY_WITH_CHILDREN, SERIALIZED_DIRECTORY_1, serialize_directory(Directory.objects.get(id=1)))
        self.assert_equal_with_unordered_distinct_lists(UNORDERED_LISTS_DIRECTORY_WITH_CHILDREN, SERIALIZED_DIRECTORY_2, serialize_directory(Directory.objects.get(id=2)))
        self.assert_equal_with_unordered_distinct_lists(UNORDERED_LISTS_DIRECTORY_WITH_CHILDREN, SERIALIZED_DIRECTORY_3, serialize_directory(Directory.objects.get(id=3)))
        self.assert_equal_with_unordered_distinct_lists(UNORDERED_LISTS_DIRECTORY_WITH_CHILDREN, SERIALIZED_DIRECTORY_4, serialize_directory(Directory.objects.get(id=4)))
        self.assert_equal_with_unordered_distinct_lists(UNORDERED_LISTS_DIRECTORY_WITH_CHILDREN, SERIALIZED_DIRECTORY_5, serialize_directory(Directory.objects.get(id=5)))
        self.assert_equal_with_unordered_distinct_lists(UNORDERED_LISTS_DIRECTORY_WITH_CHILDREN, SERIALIZED_DIRECTORY_1_WITH_CHILDREN, serialize_directory(Directory.objects.get(id=1), include_children=True))
        self.assert_equal_with_unordered_distinct_lists(UNORDERED_LISTS_DIRECTORY_WITH_CHILDREN, SERIALIZED_DIRECTORY_2_WITH_CHILDREN, serialize_directory(Directory.objects.get(id=2), include_children=True))
        self.assert_equal_with_unordered_distinct_lists(UNORDERED_LISTS_DIRECTORY_WITH_CHILDREN, SERIALIZED_DIRECTORY_3_WITH_CHILDREN, serialize_directory(Directory.objects.get(id=3), include_children=True))
        self.assert_equal_with_unordered_distinct_lists(UNORDERED_LISTS_DIRECTORY_WITH_CHILDREN, SERIALIZED_DIRECTORY_4_WITH_CHILDREN, serialize_directory(Directory.objects.get(id=4), include_children=True))
        self.assert_equal_with_unordered_distinct_lists(UNORDERED_LISTS_DIRECTORY_WITH_CHILDREN, SERIALIZED_DIRECTORY_5_WITH_CHILDREN, serialize_directory(Directory.objects.get(id=5), include_children=True))

    def test_serialize_share(self):
        self.assertEqual(SERIALIZED_SHARE_1, serialize_share(Share.objects.get(id=1)))
        self.assertEqual(SERIALIZED_SHARE_2, serialize_share(Share.objects.get(id=2)))
        self.assertEqual(SERIALIZED_SHARE_1_WITH_TARGET, serialize_share(Share.objects.get(id=1), include_target=True))
        self.assertEqual(SERIALIZED_SHARE_2_WITH_TARGET, serialize_share(Share.objects.get(id=2), include_target=True))

    def assert_equal_with_unordered_distinct_lists(self, unordered_lists, a, b):
        a = self.preprocess_unordered_distinct_lists(unordered_lists, a)
        b = self.preprocess_unordered_distinct_lists(unordered_lists, b)
        self.assertEqual(a, b)

    def preprocess_unordered_distinct_lists(self, unordered_lists, target):
        target = target.copy()
        for unordered_list in unordered_lists:
            found, dict_element, parent_dict, key_in_parent = self._find_path_in_dict(target, unordered_list)
            if found and isinstance(dict_element, list):
                list_len = len(dict_element)
                for index, element in enumerate(dict_element):
                    dict_element[index] = _ForceHashable(element)
                dict_element = set(dict_element)
                self.assertEqual(list_len, len(dict_element), msg="Expected list to contain distinct elements only, but got duplicates")
                if parent_dict is None:
                    target = dict_element
                else:
                    parent_dict[key_in_parent] = dict_element
        return target

    @staticmethod
    def _find_path_in_dict(target_dict, path):
        parent_dict: Union[dict[str, Any], None] = None
        key_in_parent: Union[str, None] = None
        element: any = target_dict
        for next_key in path:
            if next_key in element:
                parent_dict = element
                key_in_parent = next_key
                element = element[next_key]
            else:
                return False, None, None, None
        return True, element, parent_dict, key_in_parent

class _ForceHashable:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __eq__(self, other):
        if self.wrapped is None:
            return other.wrapped is None
        return self.wrapped.__eq__(other.wrapped)
    def __hash__(self):
        # Don't care about performance
        return 0
    def __str__(self):
        return "<<None>>" if self.wrapped is None else "<<" + self.wrapped.__str__() + ">>"

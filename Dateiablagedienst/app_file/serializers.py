from typing import Any

from django.db.models import QuerySet

from .models import StorageUser, File, Directory, Share

def serialize_user_info(u: StorageUser) -> dict[str, Any]:
    root = _any(u.directory_set.filter(parent_id=None))
    return {
        "personalRootDirectory": None if root is None else root.id,
        "ownShares": [
            serialize_share(s) for s in u.shares_issued.all()
        ],
        "receivedShares": [
            serialize_share(s) for s in u.shares_received.all()
        ]
    }

def serialize_storage_user(u: StorageUser) -> dict[str, Any]:
    return {
        "id": u.id,
        "displayName": u.display_name
    }

def serialize_file(f: File) -> dict[str, Any]:
    return {
        "id": f.id,
        "name": f.name,
        "owner": serialize_storage_user(f.owner),
        "parentDirectory": f.parent_directory.pk
    }

def serialize_directory(d: Directory, include_children=False) -> dict[str, Any]:
    return {
        "id": d.id,
        "name": d.name,
        "owner": serialize_storage_user(d.owner),
        **({"children": [
            {
                "type": "directory",
                "directory": serialize_directory(c)
            } for c in d.directory_set.all()
        ] + [
            {
                "type": "file",
                "file": serialize_file(c)
            } for c in d.file_set.all()
        ]} if include_children else {}),
        "parentDirectory": None if d.parent is None else d.parent.id
    }

def serialize_share(s: Share) -> dict[str, Any]:
    targets_file = s.target_file is not None
    return {
        "id": s.id,
        "issuer": serialize_storage_user(s.issuer),
        "subject": serialize_storage_user(s.subject),
        "target": {
            "type": "file" if targets_file else "directory",
            "id": s.target_file.id if targets_file else s.target_directory.id
        },
        "canWrite": s.can_write
    }

def _any(s: QuerySet):
    l = s.all()
    return l[0] if len(l) > 0 else None

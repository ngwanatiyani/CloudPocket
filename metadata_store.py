import threading
import time
from typing import Dict, List, Optional


class MetadataStore:
    def __init__(self):
        self._store: Dict[str, Dict[str, any]] = {}
        self._lock = threading.Lock()

    def add_entry(self, filename: str, s3_key: str) -> None:
        """Add a new entry to the metadata store."""
        with self._lock:
            self._store[s3_key] = {
                "filename": filename,
                "s3_key": s3_key,
                "upload_time": time.time()
            }

    def list_filenames(self) -> List[str]:
        """List all filenames in the store."""
        with self._lock:
            return [entry["filename"] for entry in self._store.values()]

    def get_entry(self, s3_key: str) -> Optional[Dict[str, any]]:
        """Get an entry by S3 key."""
        with self._lock:
            return self._store.get(s3_key)

    def remove_entry(self, s3_key: str) -> bool:
        """Remove an entry by S3 key.
        
        Returns True if removed, False if not found.
        """
        with self._lock:
            if s3_key in self._store:
                del self._store[s3_key]
                return True
            return False

    def list_s3_keys(self) -> List[str]:
        """List all S3 keys in the store."""
        with self._lock:
            return list(self._store.keys())

    def get_entry_count(self) -> int:
        """Get the total number of entries in the store."""
        with self._lock:
            return len(self._store)

    def clear(self) -> None:
        """Clear all entries from the store."""
        with self._lock:
            self._store.clear()
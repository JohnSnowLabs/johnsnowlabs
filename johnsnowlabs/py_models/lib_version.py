from typing import Optional


class LibVersion:
    """Representation of a library version in format A.B.C
    where elements can digits or X which matches all others digits"""

    def __init__(
        self,
        major_or_canonical_str: str,
        minor: Optional[str] = None,
        patch: Optional[str] = None,
    ):
        self.major, self.minor, self.patch = None, None, None

        if "." in major_or_canonical_str:

            splits = major_or_canonical_str.lower().split(".")
            if len(splits) == 0:
                raise ValueError(
                    "When using canonical representation to construct a LibVersion, format A.B.C must be used"
                )
            self.major = splits[0]
            if len(splits) > 1:
                self.minor = splits[1]
            if len(splits) > 2:
                self.patch = splits[2]

        else:
            self.major = major_or_canonical_str
            self.minor = minor
            self.patch = patch

    def equals(self: "LibVersion", lib2: "LibVersion") -> bool:
        """
        Compare two LibVersions of format A.B.C , consisting of either Digits 0-9 or x .
        X equals to any other version, i.e.  3.X.X equals 3.5.1
        A Lib Version may have the pattern A.B or A
        :param lib2:
        :return:
        """
        if self.major == lib2.major:
            if self.minor == "x" or lib2.minor == "x":
                return True

            if self.minor == lib2.minor:
                if self.patch == "x" or lib2.patch == "x":
                    return True

                if self.patch == lib2.patch:
                    return True
        return False

    def is_other_greater(self: "LibVersion", other: "LibVersion") -> bool:
        # basically  checks self < other
        if self.as_str() == other.as_str():
            return False

            # Major Check
        if self.major < other.major:
            return True
        elif self.major > other.major:
            return False

        # Minor Check
        if self.minor < other.minor:
            return True
        elif self.minor > other.minor:
            return False

        # Patch Check,
        # Patch could be missing
        if self.patch and not other.patch:
            return True
        if not self.patch and other.patch:
            return False
        # Patch could also be a str
        if (
            isinstance(self.patch, int)
            and isinstance(other.patch, int)
            and self.patch < other.patch
        ):
            return True
        if (
            isinstance(self.patch, int)
            and isinstance(other.patch, int)
            and self.patch > other.patch
        ):
            return False

        # One lib must be rc, parse it
        if isinstance(self.patch, str) and "rc" in self.patch:
            self_patch, self_rc = self.patch.split("rc")
            self_patch = int(self_patch)
            self_rc = int(self_rc)
        else:
            self_patch = self.patch
            self_rc = None

        if isinstance(other.patch, str) and "rc" in self.patch:
            other_patch, other_rc = self.patch.split("rc")
            other_patch = int(other_patch)
            other_rc = int(other_rc)

        else:
            other_patch = other.patch
            other_rc = None

        if self_patch < other_patch:
            return True
        if self_patch > other_patch:
            return True

        # One may have an rc
        if not self_rc and other_rc:
            return True
        if self_rc and not other_rc:
            return False
        # Both have no rc
        if not self_rc and not other_rc:
            return False

        # Both have a int rc
        if self_rc < other_rc:
            return True
        if self_rc > other_rc:
            return True

        # Version is equal, not an upgrade
        return False

    def as_str(self) -> str:
        """Return LibVersion object as canonical str representation"""
        # We filter out all values != None soo version checks match up
        return ".".join(filter(lambda x: x, [self.major, self.minor, self.patch]))

    def __str__(self):
        return self.as_str()
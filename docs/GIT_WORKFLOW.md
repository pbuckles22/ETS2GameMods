# Git Workflow for ETS2 Modding

This guide explains recommended git workflows for ETS2 mod development.

## Repository Structure

This repository contains multiple mods, so we use a structure that supports:
- Multiple mods in one repo
- Feature branches for each mod
- Easy collaboration
- Clean history

## Branch Strategy

### Main Branches

- **`main`** (or `master`): Production-ready mods
  - Only contains completed, tested mods
  - Each mod should be fully functional
  - Documentation should be complete

- **`develop`** (optional): Integration branch
  - For combining multiple mods before merging to main
  - Useful if you're working on multiple mods simultaneously

### Feature Branches

Create a feature branch for each mod or major feature:

```
feature/driver-id-names
feature/ticker-logger
feature/automated-training
feature/example-mod
```

**Naming Convention:**
- `feature/<mod-name>` - For new mods
- `fix/<mod-name>-<issue>` - For bug fixes
- `docs/<topic>` - For documentation updates
- `refactor/<component>` - For code refactoring

## Recommended Workflow

### Starting a New Mod

1. **Create feature branch from main:**
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/driver-id-names
   ```

2. **Develop your mod:**
   - Create mod structure
   - Add files
   - Test in-game
   - Update documentation

3. **Commit frequently:**
   ```bash
   git add mods/driver_id_names/
   git commit -m "Add driver ID mod structure"
   
   git add scripts/add_driver_ids.py
   git commit -m "Add Python script for driver ID automation"
   
   git add docs/
   git commit -m "Add documentation for driver ID mod"
   ```

4. **When mod is complete:**
   ```bash
   # Make sure everything is committed
   git status
   
   # Switch to main
   git checkout main
   
   # Merge feature branch
   git merge feature/driver-id-names
   
   # Push to remote
   git push origin main
   ```

### Working on Multiple Mods

If you're working on multiple mods simultaneously:

**Option 1: Separate feature branches**
```bash
feature/driver-id-names    # Work on mod 1
feature/ticker-logger      # Work on mod 2
```

Switch between them:
```bash
git checkout feature/driver-id-names
# Work on mod 1

git checkout feature/ticker-logger
# Work on mod 2
```

**Option 2: Use develop branch**
```bash
main
  └── develop
       ├── feature/driver-id-names
       └── feature/ticker-logger
```

Merge features into develop, then merge develop to main when ready.

## Commit Message Guidelines

### Good Commit Messages

```
Add driver ID mod structure and documentation

- Create mod directory structure
- Add manifest.sii and desc.txt
- Add comprehensive README and walkthrough
- Add Python automation script
```

```
Fix driver ID script to handle edge cases

- Fix regex pattern for names with special characters
- Add error handling for missing input file
- Update documentation with troubleshooting section
```

### Commit Message Format

```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

**Types:**
- `feat`: New feature (new mod)
- `fix`: Bug fix
- `docs`: Documentation only
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**
```
feat: Add driver ID in names mod

Creates a new mod that prepends driver IDs to names in ticker notifications.
Includes Python script for automation and comprehensive documentation.

Closes #1
```

```
fix: Correct file path in extraction guide

The walkthrough had an incorrect path for driver_names.sii location.
Updated to match actual game structure.
```

## What to Commit

### ✅ DO Commit

- Mod source files (`manifest.sii`, `desc.txt`)
- Documentation (`.md` files)
- Scripts (`.py`, `.ps1`, `.sh`)
- Project structure (directories with `.gitkeep`)
- Configuration files (`.gitignore`, etc.)

### ❌ DON'T Commit

- Built mods (`.scs` files in `dist/`)
- Extracted game files (`extracted/` directory)
- Large generated files
- IDE-specific files (already in `.gitignore`)
- Temporary files
- User-specific configurations

### Special Case: driver_names.sii

**Should you commit `driver_names.sii`?**

**Option 1: Don't commit it** (Recommended)
- It's large (hundreds of entries)
- User-specific (depends on their game version)
- Can be regenerated with the script
- Add to `.gitignore`:
  ```
  mods/*/universal/locale/*/driver_names.sii
  ```

**Option 2: Commit a sample/example**
- Commit `EXAMPLE_driver_names.sii` (already done)
- Don't commit the actual modified file
- Users generate their own with the script

**Recommendation**: Don't commit the actual `driver_names.sii` - it's too large and user-specific.

## Branch Protection (If Using GitHub/GitLab)

If you set up branch protection:

- **main branch**: Require pull requests
- **Require reviews**: Self-review is fine for personal projects
- **Require status checks**: Optional (if you add CI/CD)

## Tagging Releases

When a mod is complete and tested:

```bash
# Tag the release
git tag -a v1.0.0 -m "Driver ID mod v1.0.0 - Initial release"

# Push tags
git push origin v1.0.0
```

**Versioning:**
- `v1.0.0` - Initial release
- `v1.1.0` - New features
- `v1.0.1` - Bug fixes
- `v2.0.0` - Major changes

## Working with Remote Repository

### First Time Setup

```bash
# Initialize (if not already done)
git init

# Add remote
git remote add origin <your-repo-url>

# First commit
git add .
git commit -m "Initial commit: ETS2 modding repository structure"

# Push to remote
git push -u origin main
```

### Daily Workflow

```bash
# Start work
git checkout main
git pull origin main
git checkout -b feature/my-mod

# Make changes, commit frequently
git add .
git commit -m "Description of changes"

# Push feature branch (optional, for backup)
git push -u origin feature/my-mod

# When done, merge to main
git checkout main
git merge feature/my-mod
git push origin main

# Delete feature branch (cleanup)
git branch -d feature/my-mod
git push origin --delete feature/my-mod
```

## Handling Large Files

If you need to track large files:

**Option 1: Git LFS** (Git Large File Storage)
```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.scs"
git lfs track "mods/*/universal/**/*.sii"

# Commit .gitattributes
git add .gitattributes
```

**Option 2: Don't commit them**
- Keep large files local
- Document how to generate them
- Use scripts to automate generation

**Recommendation**: For this project, don't commit large files. Use scripts to generate them.

## Collaboration Workflow

If working with others:

1. **Fork/Clone** the repository
2. **Create feature branch** for your work
3. **Make changes** and commit
4. **Push feature branch** to your fork
5. **Create Pull Request** to main repository
6. **Review and merge** (or discuss changes)

## Troubleshooting

### "I committed a large file"

```bash
# Remove from history (if not pushed)
git reset HEAD~1

# Or use git filter-branch (advanced)
# Or use BFG Repo-Cleaner (easier)
```

### "I want to undo my last commit"

```bash
# Undo commit, keep changes
git reset --soft HEAD~1

# Undo commit, discard changes
git reset --hard HEAD~1
```

### "I want to change my last commit message"

```bash
git commit --amend -m "New commit message"
```

## Summary

**For this ETS2 modding project:**

1. ✅ Use feature branches for each mod
2. ✅ Commit frequently with clear messages
3. ✅ Don't commit built files (`.scs`) or extracted game files
4. ✅ Keep `main` branch clean and production-ready
5. ✅ Use tags for mod releases
6. ✅ Document everything (you're already doing this!)

**Example workflow:**
```
main
  ├── feature/driver-id-names → merge when complete
  ├── feature/ticker-logger → merge when complete
  └── feature/automated-training → merge when complete
```

This keeps your repository organized and makes it easy to track what each mod does! 🚛


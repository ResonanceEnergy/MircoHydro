#!/bin/bash
# ZERO DATA LOSS RECOVERY SYSTEM - MicroHydro Emergency Recovery
# Automatic restoration from backups with integrity verification

WORKSPACE="/Users/gripandripphdd/MircoHydro"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="$WORKSPACE/recovery_log_$TIMESTAMP.txt"
RECOVERY_STATUS="$WORKSPACE/recovery_status.json"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

# Logging
log() {
    local level="$1"
    local message="$2"
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo -e "[$timestamp] [$level] $message" >> "$LOG_FILE"
    echo -e "[$timestamp] [$level] $message"
}

# Update recovery status
update_recovery_status() {
    local phase="$1"
    local status="$2"
    local details="$3"

    local status_data="{\"phase\": \"$phase\", \"status\": \"$status\", \"details\": \"$details\", \"timestamp\": \"$(date +"%Y-%m-%d %H:%M:%S")\"}"

    echo "$status_data" > "$RECOVERY_STATUS"
}

# Find latest backup
find_latest_backup() {
    log "BACKUP" "Searching for latest backup..."

    # Look for backup directories
    local backup_dirs=$(find "$WORKSPACE" -maxdepth 1 -type d -name "_MASTER_BACKUPS_*" -o -name "_SCHEDULED_BACKUP_*" | sort -r)

    if [ -z "$backup_dirs" ]; then
        log "ERROR" "No backup directories found"
        return 1
    fi

    # Get the most recent backup
    LATEST_BACKUP=$(echo "$backup_dirs" | head -1)
    log "BACKUP" "Latest backup found: $LATEST_BACKUP"

    return 0
}

# Verify backup integrity
verify_backup_integrity() {
    local backup_dir="$1"
    log "VERIFY" "Verifying backup integrity: $backup_dir"

    # Check if backup directory exists and has content
    if [ ! -d "$backup_dir" ]; then
        log "ERROR" "Backup directory does not exist: $backup_dir"
        return 1
    fi

    # Count files in backup
    local backup_file_count=$(find "$backup_dir" -type f | wc -l)
    log "VERIFY" "Backup contains $backup_file_count files"

    if [ "$backup_file_count" -eq 0 ]; then
        log "ERROR" "Backup directory is empty"
        return 1
    fi

    # Check critical files exist in backup
    local critical_files=(
        "complete_automation_system.py"
        "master_automation_orchestrator.py"
        "AUTOMATION_README.md"
        "READY_TO_EXECUTE_TOOLKIT.md"
    )

    local missing_critical=""
    for file in "${critical_files[@]}"; do
        if [ ! -f "$backup_dir/$file" ]; then
            missing_critical="$missing_critical $file"
        fi
    done

    if [ -n "$missing_critical" ]; then
        log "ERROR" "Critical files missing from backup:$missing_critical"
        return 1
    fi

    log "VERIFY" "Backup integrity verified successfully"
    return 0
}

# Create pre-recovery backup
create_pre_recovery_backup() {
    log "BACKUP" "Creating pre-recovery backup..."

    local pre_recovery_dir="$WORKSPACE/_PRE_RECOVERY_BACKUP_$TIMESTAMP"
    mkdir -p "$pre_recovery_dir" || {
        log "ERROR" "Failed to create pre-recovery backup directory"
        return 1
    }

    # Backup current state (excluding backup directories)
    rsync -a --exclude='_BACKUPS' --exclude='_CONSOLIDATION_BACKUP' \
          --exclude='_MASTER_BACKUPS_*' --exclude='_SCHEDULED_BACKUP_*' \
          --exclude='_PRE_RECOVERY_BACKUP_*' \
          "$WORKSPACE/" "$pre_recovery_dir/" 2>/dev/null || {
        log "ERROR" "Pre-recovery backup failed"
        return 1
    }

    PRE_RECOVERY_BACKUP="$pre_recovery_dir"
    log "BACKUP" "Pre-recovery backup created: $PRE_RECOVERY_BACKUP"
    return 0
}

# Perform selective recovery
selective_recovery() {
    local backup_dir="$1"
    local recovery_type="$2"  # "full" or "selective"

    log "RECOVERY" "Starting $recovery_type recovery from: $backup_dir"

    if [ "$recovery_type" = "full" ]; then
        # Full recovery - restore everything
        log "RECOVERY" "Performing full recovery..."

        # Create recovery staging area
        local staging_dir="$WORKSPACE/_RECOVERY_STAGING_$TIMESTAMP"
        mkdir -p "$staging_dir"

        # Copy backup to staging
        rsync -a "$backup_dir/" "$staging_dir/" || {
            log "ERROR" "Failed to stage backup for recovery"
            return 1
        }

        # Verify staging integrity
        if ! verify_backup_integrity "$staging_dir"; then
            log "ERROR" "Staging area integrity check failed"
            rm -rf "$staging_dir"
            return 1
        fi

        # Perform recovery (overwrite current workspace)
        rsync -a --delete "$staging_dir/" "$WORKSPACE/" || {
            log "ERROR" "Recovery operation failed"
            return 1
        }

        # Cleanup staging
        rm -rf "$staging_dir"

    else
        # Selective recovery - restore only critical components
        log "RECOVERY" "Performing selective recovery (critical components only)..."

        local critical_components=(
            "complete_automation_system.py"
            "master_automation_orchestrator.py"
            "AUTOMATION_README.md"
            "MANUAL_EXECUTION_GUIDE.md"
            "READY_TO_EXECUTE_TOOLKIT.md"
            "Engineering"
            "Research"
            "Implementation"
        )

        for component in "${critical_components[@]}"; do
            if [ -e "$backup_dir/$component" ]; then
                if [ -d "$backup_dir/$component" ]; then
                    # Directory
                    mkdir -p "$WORKSPACE/$component"
                    rsync -a "$backup_dir/$component/" "$WORKSPACE/$component/" || {
                        log "ERROR" "Failed to recover directory: $component"
                        continue
                    }
                else
                    # File
                    rsync -a "$backup_dir/$component" "$WORKSPACE/$component" || {
                        log "ERROR" "Failed to recover file: $component"
                        continue
                    }
                fi
                log "RECOVERY" "Recovered: $component"
            else
                log "WARNING" "Component not found in backup: $component"
            fi
        done
    fi

    log "RECOVERY" "Recovery operation completed"
    return 0
}

# Post-recovery verification
post_recovery_verification() {
    log "VERIFY" "Performing post-recovery verification..."

    local verification_passed=true

    # Check critical files
    local critical_files=(
        "complete_automation_system.py"
        "master_automation_orchestrator.py"
        "AUTOMATION_README.md"
        "READY_TO_EXECUTE_TOOLKIT.md"
    )

    for file in "${critical_files[@]}"; do
        if [ ! -f "$WORKSPACE/$file" ]; then
            log "ERROR" "Critical file missing after recovery: $file"
            verification_passed=false
        fi
    done

    # Check critical directories
    local critical_dirs=("Engineering" "Research" "Implementation")
    for dir in "${critical_dirs[@]}"; do
        if [ ! -d "$WORKSPACE/$dir" ]; then
            log "ERROR" "Critical directory missing after recovery: $dir"
            verification_passed=false
        fi
    done

    if [ "$verification_passed" = true ]; then
        log "VERIFY" "Post-recovery verification PASSED"
        return 0
    else
        log "ERROR" "Post-recovery verification FAILED"
        return 1
    fi
}

# Rollback recovery
rollback_recovery() {
    log "ROLLBACK" "Initiating recovery rollback..."

    if [ -n "$PRE_RECOVERY_BACKUP" ] && [ -d "$PRE_RECOVERY_BACKUP" ]; then
        log "ROLLBACK" "Rolling back to pre-recovery state: $PRE_RECOVERY_BACKUP"

        # Restore from pre-recovery backup
        rsync -a --delete "$PRE_RECOVERY_BACKUP/" "$WORKSPACE/" || {
            log "ERROR" "Rollback operation failed"
            return 1
        }

        log "ROLLBACK" "Recovery rollback completed successfully"
        return 0
    else
        log "ERROR" "No pre-recovery backup available for rollback"
        return 1
    fi
}

# Main recovery function
main() {
    echo -e "${PURPLE}🛟 ZERO DATA LOSS RECOVERY SYSTEM - MICROHYDRO EMERGENCY RECOVERY${NC}"
    echo -e "${PURPLE}=====================================================================${NC}"
    echo ""

    local recovery_type="${1:-selective}"  # Default to selective recovery

    log "INIT" "Recovery system started - Type: $recovery_type"

    update_recovery_status "init" "started" "Recovery system initialized"

    # Phase 1: Find latest backup
    update_recovery_status "backup_search" "in_progress" "Searching for latest backup"
    if ! find_latest_backup; then
        update_recovery_status "backup_search" "failed" "No backup found"
        log "ERROR" "Recovery failed: No backup available"
        echo -e "${RED}❌ RECOVERY FAILED: No backup available${NC}"
        exit 1
    fi
    update_recovery_status "backup_search" "completed" "Latest backup: $LATEST_BACKUP"

    # Phase 2: Verify backup integrity
    update_recovery_status "backup_verify" "in_progress" "Verifying backup integrity"
    if ! verify_backup_integrity "$LATEST_BACKUP"; then
        update_recovery_status "backup_verify" "failed" "Backup integrity check failed"
        log "ERROR" "Recovery failed: Backup integrity check failed"
        echo -e "${RED}❌ RECOVERY FAILED: Backup integrity compromised${NC}"
        exit 1
    fi
    update_recovery_status "backup_verify" "completed" "Backup integrity verified"

    # Phase 3: Create pre-recovery backup
    update_recovery_status "pre_recovery_backup" "in_progress" "Creating pre-recovery backup"
    if ! create_pre_recovery_backup; then
        update_recovery_status "pre_recovery_backup" "failed" "Pre-recovery backup failed"
        log "ERROR" "Recovery failed: Could not create pre-recovery backup"
        echo -e "${RED}❌ RECOVERY FAILED: Could not create safety backup${NC}"
        exit 1
    fi
    update_recovery_status "pre_recovery_backup" "completed" "Pre-recovery backup: $PRE_RECOVERY_BACKUP"

    # Phase 4: Perform recovery
    update_recovery_status "recovery" "in_progress" "Performing $recovery_type recovery"
    if ! selective_recovery "$LATEST_BACKUP" "$recovery_type"; then
        update_recovery_status "recovery" "failed" "Recovery operation failed"

        # Attempt rollback
        update_recovery_status "rollback" "in_progress" "Attempting rollback"
        if rollback_recovery; then
            update_recovery_status "rollback" "completed" "Rollback successful"
            log "ERROR" "Recovery failed but rollback successful"
            echo -e "${YELLOW}⚠️  RECOVERY FAILED: System rolled back to pre-recovery state${NC}"
            exit 1
        else
            update_recovery_status "rollback" "failed" "Rollback failed"
            log "CRITICAL" "Recovery and rollback both failed"
            echo -e "${RED}🚨 CRITICAL: Recovery and rollback both failed${NC}"
            exit 1
        fi
    fi
    update_recovery_status "recovery" "completed" "$recovery_type recovery successful"

    # Phase 5: Post-recovery verification
    update_recovery_status "post_verify" "in_progress" "Performing post-recovery verification"
    if ! post_recovery_verification; then
        update_recovery_status "post_verify" "failed" "Post-recovery verification failed"

        # Attempt rollback
        update_recovery_status "rollback" "in_progress" "Attempting rollback due to verification failure"
        if rollback_recovery; then
            update_recovery_status "rollback" "completed" "Rollback successful"
            log "ERROR" "Recovery verification failed, system rolled back"
            echo -e "${YELLOW}⚠️  RECOVERY VERIFICATION FAILED: System rolled back${NC}"
            exit 1
        else
            update_recovery_status "rollback" "failed" "Rollback failed"
            log "CRITICAL" "Recovery verification failed and rollback failed"
            echo -e "${RED}🚨 CRITICAL: Recovery verification failed and rollback failed${NC}"
            exit 1
        fi
    fi
    update_recovery_status "post_verify" "completed" "Post-recovery verification passed"

    # Success
    update_recovery_status "complete" "success" "Zero data loss recovery completed successfully"

    log "SUCCESS" "Zero data loss recovery completed successfully"
    echo ""
    echo -e "${GREEN}🎉 ZERO DATA LOSS RECOVERY COMPLETED SUCCESSFULLY!${NC}"
    echo ""
    echo -e "${BLUE}📊 RECOVERY SUMMARY:${NC}"
    echo -e "   ✅ Backup source: $LATEST_BACKUP"
    echo -e "   ✅ Recovery type: $recovery_type"
    echo -e "   ✅ Safety backup: $PRE_RECOVERY_BACKUP"
    echo -e "   ✅ Verification: PASSED"
    echo ""
    echo -e "${BLUE}📁 RECOVERY LOGS:${NC}"
    echo -e "   📄 Recovery log: $LOG_FILE"
    echo -e "   📊 Recovery status: $RECOVERY_STATUS"
    echo ""
    echo -e "${YELLOW}🔄 NEXT STEPS:${NC}"
    echo -e "   1. Verify system functionality"
    echo -e "   2. Run automation tests"
    echo -e "   3. Resume continuous operations"
    echo ""
}

# Run main function with argument
main "$@"
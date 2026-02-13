#!/bin/bash
# MASTER OPERATIONS DASHBOARD - MicroHydro Unified Control Center
# Consolidated interface for all launch systems, continuous operations, and recovery

WORKSPACE="/Users/gripandripphdd/MircoHydro"
DASHBOARD_LOG="$WORKSPACE/dashboard_log_$(date +"%Y%m%d_%H%M%S").txt"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

# Dashboard functions
show_header() {
    clear
    echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}║${WHITE}                    MASTER OPERATIONS DASHBOARD${NC}                               ${PURPLE}║${NC}"
    echo -e "${PURPLE}║${WHITE}                   MICROHYDRO UNIFIED CONTROL CENTER${NC}                        ${PURPLE}║${NC}"
    echo -e "${PURPLE}║${WHITE}                 🚀 ZERO DATA LOSS • 24/7 OPERATIONS${NC}                      ${PURPLE}║${NC}"
    echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

show_menu() {
    echo -e "${CYAN}┌─ AVAILABLE OPERATIONS ──────────────────────────────────────────────────────┐${NC}"
    echo -e "${CYAN}│${NC}                                                                           ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  ${GREEN}1.${NC} 🚀 LAUNCH MASTER SYSTEM          ${WHITE}│${NC} Complete automation + AI deployment  ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  ${GREEN}2.${NC} 🔄 START CONTINUOUS OPS         ${WHITE}│${NC} 24/7 monitoring + auto-recovery      ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  ${GREEN}3.${NC} 🛟 EMERGENCY RECOVERY           ${WHITE}│${NC} Zero data loss restoration           ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  ${GREEN}4.${NC} 📊 SYSTEM STATUS                ${WHITE}│${NC} Real-time health monitoring           ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  ${GREEN}5.${NC} 💾 BACKUP OPERATIONS           ${WHITE}│${NC} Manual backup creation               ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  ${GREEN}6.${NC} 🔧 MAINTENANCE MODE            ${WHITE}│${NC} System maintenance tools             ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  ${GREEN}7.${NC} 📋 VIEW LOGS                    ${WHITE}│${NC} Access system logs                    ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  ${GREEN}8.${NC} ⚙️  CONFIGURATION               ${WHITE}│${NC} System configuration                 ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  ${GREEN}9.${NC} 🆘 HELP & DOCUMENTATION        ${WHITE}│${NC} User guides and troubleshooting       ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  ${GREEN}0.${NC} 🚪 EXIT DASHBOARD             ${WHITE}│${NC} Close dashboard                       ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}                                                                           ${CYAN}│${NC}"
    echo -e "${CYAN}└───────────────────────────────────────────────────────────────────────────┘${NC}"
    echo ""
}

show_system_status() {
    echo -e "${BLUE}┌─ SYSTEM STATUS ────────────────────────────────────────────────────────────┐${NC}"
    echo -e "${BLUE}│${NC}                                                                           ${BLUE}│${NC}"

    # Check workspace
    if [ -d "$WORKSPACE" ]; then
        echo -e "${BLUE}│${NC}  ${GREEN}✓${NC} Workspace:              $WORKSPACE                              ${BLUE}│${NC}"
    else
        echo -e "${BLUE}│${NC}  ${RED}✗${NC} Workspace:              $WORKSPACE                              ${BLUE}│${NC}"
    fi

    # Check critical files
    local critical_files=("complete_automation_system.py" "AUTOMATION_README.md" "READY_TO_EXECUTE_TOOLKIT.md")
    local files_ok=true
    for file in "${critical_files[@]}"; do
        if [ ! -f "$WORKSPACE/$file" ]; then
            files_ok=false
            break
        fi
    done

    if [ "$files_ok" = true ]; then
        echo -e "${BLUE}│${NC}  ${GREEN}✓${NC} Critical Files:          Present                                   ${BLUE}│${NC}"
    else
        echo -e "${BLUE}│${NC}  ${RED}✗${NC} Critical Files:          Missing                                   ${BLUE}│${NC}"
    fi

    # Check directories
    local dirs_ok=true
    for dir in "Engineering" "Research" "Implementation"; do
        if [ ! -d "$WORKSPACE/$dir" ]; then
            dirs_ok=false
            break
        fi
    done

    if [ "$dirs_ok" = true ]; then
        echo -e "${BLUE}│${NC}  ${GREEN}✓${NC} Core Directories:        Present                                   ${BLUE}│${NC}"
    else
        echo -e "${BLUE}│${NC}  ${RED}✗${NC} Core Directories:        Missing                                   ${BLUE}│${NC}"
    fi

    # Check disk space
    local disk_usage=$(df "$WORKSPACE" 2>/dev/null | tail -1 | awk '{print $5}' | sed 's/%//')
    if [ -n "$disk_usage" ]; then
        if [ "$disk_usage" -gt 90 ]; then
            echo -e "${BLUE}│${NC}  ${RED}✗${NC} Disk Space:              ${disk_usage}%% used (CRITICAL)                   ${BLUE}│${NC}"
        elif [ "$disk_usage" -gt 80 ]; then
            echo -e "${BLUE}│${NC}  ${YELLOW}⚠${NC} Disk Space:              ${disk_usage}%% used (WARNING)                    ${BLUE}│${NC}"
        else
            echo -e "${BLUE}│${NC}  ${GREEN}✓${NC} Disk Space:              ${disk_usage}%% used                                   ${BLUE}│${NC}"
        fi
    else
        echo -e "${BLUE}│${NC}  ${YELLOW}?${NC} Disk Space:              Unable to check                            ${BLUE}│${NC}"
    fi

    # Check running processes
    local automation_running=$(pgrep -f "python.*automation" 2>/dev/null | wc -l)
    local monitoring_running=$(pgrep -f "continuous_monitor" 2>/dev/null | wc -l)

    if [ "$automation_running" -gt 0 ]; then
        echo -e "${BLUE}│${NC}  ${GREEN}✓${NC} Automation Processes:    $automation_running running                          ${BLUE}│${NC}"
    else
        echo -e "${BLUE}│${NC}  ${YELLOW}⚠${NC} Automation Processes:    None detected                             ${BLUE}│${NC}"
    fi

    if [ "$monitoring_running" -gt 0 ]; then
        echo -e "${BLUE}│${NC}  ${GREEN}✓${NC} Monitoring Processes:     $monitoring_running running                         ${BLUE}│${NC}"
    else
        echo -e "${BLUE}│${NC}  ${YELLOW}⚠${NC} Monitoring Processes:     None detected                             ${BLUE}│${NC}"
    fi

    # Check latest backup
    local latest_backup=$(find "$WORKSPACE" -maxdepth 1 -type d -name "_MASTER_BACKUPS_*" -o -name "_SCHEDULED_BACKUP_*" 2>/dev/null | sort -r | head -1)
    if [ -n "$latest_backup" ]; then
        local backup_age=$(($(date +%s) - $(stat -f %m "$latest_backup" 2>/dev/null || date -r "$latest_backup" +%s 2>/dev/null || echo $(date +%s))))
        local backup_hours=$((backup_age / 3600))
        if [ "$backup_hours" -lt 24 ]; then
            echo -e "${BLUE}│${NC}  ${GREEN}✓${NC} Latest Backup:           ${backup_hours}h ago                                 ${BLUE}│${NC}"
        else
            echo -e "${BLUE}│${NC}  ${YELLOW}⚠${NC} Latest Backup:           ${backup_hours}h ago                                 ${BLUE}│${NC}"
        fi
    else
        echo -e "${BLUE}│${NC}  ${RED}✗${NC} Latest Backup:           None found                                ${BLUE}│${NC}"
    fi

    echo -e "${BLUE}│${NC}                                                                           ${BLUE}│${NC}"
    echo -e "${BLUE}└───────────────────────────────────────────────────────────────────────────┘${NC}"
    echo ""
}

execute_operation() {
    local choice="$1"

    case $choice in
        1)
            echo -e "${GREEN}🚀 LAUNCHING MASTER SYSTEM...${NC}"
            echo ""
            if [ -f "$WORKSPACE/UNIVERSAL_MASTER_LAUNCH.sh" ]; then
                chmod +x "$WORKSPACE/UNIVERSAL_MASTER_LAUNCH.sh"
                "$WORKSPACE/UNIVERSAL_MASTER_LAUNCH.sh"
            else
                echo -e "${RED}❌ Master launch system not found${NC}"
            fi
            echo ""
            read -p "Press Enter to continue..."
            ;;

        2)
            echo -e "${GREEN}🔄 STARTING CONTINUOUS OPERATIONS...${NC}"
            echo ""
            if [ -f "$WORKSPACE/CONTINUOUS_OPERATIONS_MANAGER.sh" ]; then
                chmod +x "$WORKSPACE/CONTINUOUS_OPERATIONS_MANAGER.sh"
                nohup "$WORKSPACE/CONTINUOUS_OPERATIONS_MANAGER.sh" > /dev/null 2>&1 &
                echo -e "${GREEN}✅ Continuous operations started in background${NC}"
            else
                echo -e "${RED}❌ Continuous operations manager not found${NC}"
            fi
            echo ""
            read -p "Press Enter to continue..."
            ;;

        3)
            echo -e "${YELLOW}🛟 INITIATING EMERGENCY RECOVERY...${NC}"
            echo ""
            echo -e "${YELLOW}Select recovery type:${NC}"
            echo "1. Selective Recovery (critical components only)"
            echo "2. Full Recovery (complete system restore)"
            echo ""
            read -p "Enter choice (1-2): " recovery_choice

            case $recovery_choice in
                1)
                    if [ -f "$WORKSPACE/ZERO_DATA_LOSS_RECOVERY.sh" ]; then
                        chmod +x "$WORKSPACE/ZERO_DATA_LOSS_RECOVERY.sh"
                        "$WORKSPACE/ZERO_DATA_LOSS_RECOVERY.sh" selective
                    else
                        echo -e "${RED}❌ Recovery system not found${NC}"
                    fi
                    ;;
                2)
                    if [ -f "$WORKSPACE/ZERO_DATA_LOSS_RECOVERY.sh" ]; then
                        chmod +x "$WORKSPACE/ZERO_DATA_LOSS_RECOVERY.sh"
                        "$WORKSPACE/ZERO_DATA_LOSS_RECOVERY.sh" full
                    else
                        echo -e "${RED}❌ Recovery system not found${NC}"
                    fi
                    ;;
                *)
                    echo -e "${RED}❌ Invalid choice${NC}"
                    ;;
            esac
            echo ""
            read -p "Press Enter to continue..."
            ;;

        4)
            show_system_status
            read -p "Press Enter to continue..."
            ;;

        5)
            echo -e "${BLUE}💾 BACKUP OPERATIONS${NC}"
            echo ""
            echo -e "${BLUE}Select backup type:${NC}"
            echo "1. Quick Backup (critical files only)"
            echo "2. Full Backup (complete system)"
            echo "3. Scheduled Backup Status"
            echo ""
            read -p "Enter choice (1-3): " backup_choice

            case $backup_choice in
                1)
                    echo -e "${GREEN}Creating quick backup...${NC}"
                    local backup_dir="$WORKSPACE/_QUICK_BACKUP_$(date +"%Y%m%d_%H%M%S")"
                    mkdir -p "$backup_dir"
                    cp "$WORKSPACE/complete_automation_system.py" "$backup_dir/" 2>/dev/null
                    cp "$WORKSPACE/AUTOMATION_README.md" "$backup_dir/" 2>/dev/null
                    cp "$WORKSPACE/READY_TO_EXECUTE_TOOLKIT.md" "$backup_dir/" 2>/dev/null
                    echo -e "${GREEN}✅ Quick backup created: $backup_dir${NC}"
                    ;;
                2)
                    echo -e "${GREEN}Creating full backup...${NC}"
                    local backup_dir="$WORKSPACE/_FULL_BACKUP_$(date +"%Y%m%d_%H%M%S")"
                    mkdir -p "$backup_dir"
                    rsync -a --exclude='.git' --exclude='node_modules' "$WORKSPACE/" "$backup_dir/"
                    echo -e "${GREEN}✅ Full backup created: $backup_dir${NC}"
                    ;;
                3)
                    echo -e "${BLUE}Scheduled Backup Status:${NC}"
                    local scheduled_backups=$(find "$WORKSPACE" -maxdepth 1 -type d -name "_SCHEDULED_BACKUP_*" | wc -l)
                    local latest_scheduled=$(find "$WORKSPACE" -maxdepth 1 -type d -name "_SCHEDULED_BACKUP_*" | sort -r | head -1)
                    echo "Total scheduled backups: $scheduled_backups"
                    if [ -n "$latest_scheduled" ]; then
                        echo "Latest scheduled backup: $(basename "$latest_scheduled")"
                    fi
                    ;;
                *)
                    echo -e "${RED}❌ Invalid choice${NC}"
                    ;;
            esac
            echo ""
            read -p "Press Enter to continue..."
            ;;

        6)
            echo -e "${YELLOW}🔧 MAINTENANCE MODE${NC}"
            echo ""
            echo -e "${YELLOW}Select maintenance operation:${NC}"
            echo "1. Clean old logs (7+ days)"
            echo "2. Verify file integrity"
            echo "3. Reset monitoring processes"
            echo "4. Update permissions"
            echo ""
            read -p "Enter choice (1-4): " maint_choice

            case $maint_choice in
                1)
                    echo -e "${GREEN}Cleaning old logs...${NC}"
                    find "$WORKSPACE" -name "*.log" -mtime +7 -delete 2>/dev/null
                    echo -e "${GREEN}✅ Old logs cleaned${NC}"
                    ;;
                2)
                    echo -e "${GREEN}Verifying file integrity...${NC}"
                    local total_files=$(find "$WORKSPACE" -type f | wc -l)
                    local readable_files=$(find "$WORKSPACE" -type f -readable | wc -l)
                    echo "Total files: $total_files"
                    echo "Readable files: $readable_files"
                    if [ "$total_files" -eq "$readable_files" ]; then
                        echo -e "${GREEN}✅ All files readable${NC}"
                    else
                        echo -e "${RED}⚠️  Some files may be corrupted${NC}"
                    fi
                    ;;
                3)
                    echo -e "${GREEN}Resetting monitoring processes...${NC}"
                    pkill -f "continuous_monitor" 2>/dev/null
                    pkill -f "continuous_ops" 2>/dev/null
                    rm -f "$WORKSPACE/monitoring.pid" "$WORKSPACE/continuous_ops.pid" 2>/dev/null
                    echo -e "${GREEN}✅ Monitoring processes reset${NC}"
                    ;;
                4)
                    echo -e "${GREEN}Updating permissions...${NC}"
                    find "$WORKSPACE" -name "*.sh" -exec chmod +x {} \; 2>/dev/null
                    find "$WORKSPACE" -name "*.py" -exec chmod +x {} \; 2>/dev/null
                    echo -e "${GREEN}✅ Permissions updated${NC}"
                    ;;
                *)
                    echo -e "${RED}❌ Invalid choice${NC}"
                    ;;
            esac
            echo ""
            read -p "Press Enter to continue..."
            ;;

        7)
            echo -e "${BLUE}📋 SYSTEM LOGS${NC}"
            echo ""
            echo -e "${BLUE}Select log type:${NC}"
            echo "1. Dashboard logs"
            echo "2. Automation logs"
            echo "3. Recovery logs"
            echo "4. Continuous ops logs"
            echo "5. All recent logs"
            echo ""
            read -p "Enter choice (1-5): " log_choice

            case $log_choice in
                1)
                    echo -e "${CYAN}Dashboard logs:${NC}"
                    ls -la "$WORKSPACE/dashboard_log_"* 2>/dev/null || echo "No dashboard logs found"
                    ;;
                2)
                    echo -e "${CYAN}Automation logs:${NC}"
                    ls -la "$WORKSPACE/automation_log_"* 2>/dev/null || echo "No automation logs found"
                    ;;
                3)
                    echo -e "${CYAN}Recovery logs:${NC}"
                    ls -la "$WORKSPACE/recovery_log_"* 2>/dev/null || echo "No recovery logs found"
                    ;;
                4)
                    echo -e "${CYAN}Continuous ops logs:${NC}"
                    ls -la "$WORKSPACE/continuous_ops_"* 2>/dev/null || echo "No continuous ops logs found"
                    ;;
                5)
                    echo -e "${CYAN}All recent logs:${NC}"
                    find "$WORKSPACE" -name "*.log" -mtime -1 -exec ls -la {} \; 2>/dev/null | head -10
                    ;;
                *)
                    echo -e "${RED}❌ Invalid choice${NC}"
                    ;;
            esac
            echo ""
            read -p "Press Enter to continue..."
            ;;

        8)
            echo -e "${PURPLE}⚙️  SYSTEM CONFIGURATION${NC}"
            echo ""
            echo -e "${PURPLE}Current configuration:${NC}"
            echo "Workspace: $WORKSPACE"
            echo "Python requirement: 3.6+"
            echo "Backup frequency: Daily (2 AM)"
            echo "Monitoring interval: 5-15 minutes"
            echo "Log retention: 7 days"
            echo ""
            echo -e "${YELLOW}Configuration options coming in next version${NC}"
            echo ""
            read -p "Press Enter to continue..."
            ;;

        9)
            echo -e "${CYAN}🆘 HELP & DOCUMENTATION${NC}"
            echo ""
            echo -e "${CYAN}Available documentation:${NC}"
            echo "• AUTOMATION_README.md - Complete system documentation"
            echo "• MANUAL_EXECUTION_GUIDE.md - Step-by-step execution guide"
            echo "• READY_TO_EXECUTE_TOOLKIT.md - Operational procedures"
            echo ""
            echo -e "${CYAN}Quick help:${NC}"
            echo "• Use option 1 to launch the complete system"
            echo "• Use option 2 for 24/7 continuous operations"
            echo "• Use option 3 only in emergency situations"
            echo "• Check option 4 regularly for system health"
            echo ""
            read -p "Press Enter to continue..."
            ;;

        0)
            echo -e "${GREEN}👋 Thank you for using MicroHydro Master Operations Dashboard${NC}"
            echo -e "${GREEN}System will continue running in background if continuous operations are active.${NC}"
            echo ""
            exit 0
            ;;

        *)
            echo -e "${RED}❌ Invalid choice. Please select 0-9.${NC}"
            echo ""
            read -p "Press Enter to continue..."
            ;;
    esac
}

# Main dashboard loop
main() {
    # Check if we're in the right directory
    if [ ! -d "$WORKSPACE" ]; then
        echo -e "${RED}❌ Error: Workspace directory not found: $WORKSPACE${NC}"
        exit 1
    fi

    cd "$WORKSPACE" || exit 1

    while true; do
        show_header
        show_system_status
        show_menu

        read -p "Enter your choice (0-9): " choice
        echo ""

        execute_operation "$choice"
    done
}

# Run main dashboard
main "$@"
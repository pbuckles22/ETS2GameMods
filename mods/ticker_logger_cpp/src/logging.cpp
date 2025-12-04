// Logging implementation

#include "logging.h"
#include <fstream>
#include <ctime>
#include <windows.h>
#include <shlobj.h>
#include <sstream>

static std::ofstream logFile;
static std::string logFilePath;

std::string GetLogFilePath()
{
    // Get Documents folder path
    char documentsPath[MAX_PATH];
    if (SUCCEEDED(SHGetFolderPathA(NULL, CSIDL_PERSONAL, NULL, SHGFP_TYPE_CURRENT, documentsPath)))
    {
        std::string path = std::string(documentsPath) + "\\Euro Truck Simulator 2\\ticker_log.txt";
        return path;
    }
    
    // Fallback to current directory
    return "ticker_log.txt";
}

std::string GetCurrentTimestamp()
{
    auto now = std::time(nullptr);
    auto tm = *std::localtime(&now);
    
    std::ostringstream oss;
    oss << std::put_time(&tm, "%Y-%m-%d %H:%M:%S");
    return oss.str();
}

void InitializeLogging()
{
    logFilePath = GetLogFilePath();
    logFile.open(logFilePath, std::ios::app);
    
    if (logFile.is_open())
    {
        logFile << "\n=== Ticker Logger Started: " << GetCurrentTimestamp() << " ===\n";
        logFile.flush();
    }
}

void CloseLogging()
{
    if (logFile.is_open())
    {
        logFile << "=== Ticker Logger Stopped: " << GetCurrentTimestamp() << " ===\n\n";
        logFile.close();
    }
}

void LogTickerMessage(const std::string& message)
{
    if (logFile.is_open())
    {
        logFile << "[" << GetCurrentTimestamp() << "] " << message << "\n";
        logFile.flush();
    }
}

void LogMessage(const std::string& message)
{
    if (logFile.is_open())
    {
        logFile << "[" << GetCurrentTimestamp() << "] [INFO] " << message << "\n";
        logFile.flush();
    }
}

void LogError(const std::string& error)
{
    if (logFile.is_open())
    {
        logFile << "[" << GetCurrentTimestamp() << "] [ERROR] " << error << "\n";
        logFile.flush();
    }
}


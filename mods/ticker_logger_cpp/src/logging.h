// Logging functionality header

#pragma once
#include <string>

// Initialize logging system
void InitializeLogging();

// Close logging system
void CloseLogging();

// Log a ticker message
void LogTickerMessage(const std::string& message);

// Log a general message
void LogMessage(const std::string& message);

// Log an error
void LogError(const std::string& error);


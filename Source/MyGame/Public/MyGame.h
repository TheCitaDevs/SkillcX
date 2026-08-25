// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"

/**
 * MyGame Module - Foundation for 4-player co-op boss-rush roguelike
 * 
 * Architecture: Server-authoritative, GAS-based, data-driven
 * Engine: Unreal Engine 5.8.2
 */
class FMyGameModule : public IModuleInterface
{
public:
	/** IModuleInterface implementation */
	virtual void StartupModule() override;
	virtual void ShutdownModule() override;

	/** Returns true if this module is loaded */
	static inline bool IsAvailable() { return FModuleManager::Get().IsModuleLoaded("MyGame"); }
};

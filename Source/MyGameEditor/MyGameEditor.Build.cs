// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class MyGameEditor : ModuleRules
{
	public MyGameEditor(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.PCHOrSharedThroughUnity;
		
		PublicDependencyModuleNames.AddRange(new string[] 
		{ 
			"Core",
			"CoreUObject",
			"Engine",
			"UnrealEd",
			
			// Editor tools for GAS, PCG, and Multiplayer
			"GameplayAbilities",
			"GameplayTags",
			"GameplayTasks",
			"PCG",
			"PCGGraph",
			"PCGHelpers",
			
			// Automation & Testing
			"AutomationController",
			"FunctionalTesting",
			"AutomatedTaskSystem"
		});

		PrivateDependencyModuleNames.AddRange(new string[] 
		{ 
			"Slate",
			"SlateCore",
			"MyGame"
		});

		bEnableExceptions = false;
		bTreatWarningsAsErrors = true;
	}
}

// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class MyGame : ModuleRules
{
	public MyGame(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.PCHOrSharedThroughUnity;
		PublicDependencyModuleNames.AddRange(new string[] 
		{ 
			"Core",
			"CoreUObject",
			"Engine",
			"InputCore",
			"EnhancedInput",
			
			// Gameplay Ability System (GAS)
			"GameplayAbilities",
			"GameplayTags",
			"GameplayTasks",
			
			// Online Multiplayer (Server-authoritative)
			"OnlineSubsystem",
			"OnlineSubsystemUtils",
			"Sockets",
			"Networking",
			
			// PCG (Procedural Content Generation)
			"PCG",
			"PCGGraph",
			"PCGHelpers",
			
			// Unreal MCP (Model Context Protocol) Foundation
			"ModelClient",
			
			// Automation & Testing
			"AutomationController",
			"FunctionalTesting",
			
			// Data-driven systems
			"Json",
			"JsonUtilities"
		});

		PrivateDependencyModuleNames.AddRange(new string[] 
		{ 
			"Slate",
			"SlateCore"
		});

		// Server-only builds exclude editor modules
		if (Target.Type == TargetType.Server)
		{
			PublicDependencyModuleNames.RemoveAll(Module => 
				Module.Contains("Slate") || Module.Contains("Editor"));
		}

		// Enable strict compilation for commercial provenance
		bEnableExceptions = false;
		bTreatWarningsAsErrors = true;
		
		// Optimize for shipping builds
		PublicDefinitions.Add("WITH_SERVER_CODE=1");
	}
}
